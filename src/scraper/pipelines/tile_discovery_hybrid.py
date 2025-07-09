import math
import asyncio
from pathlib import Path
import json
from typing import List, Set, Tuple

import httpx
import structlog
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.exc import SQLAlchemyError

from scraper.utils.config import get_discovery_config
from scraper.db.engine import get_async_db_engine, get_async_session
from scraper.db.models import tile_state

logger = structlog.get_logger()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
config = get_discovery_config()
TILE_SERVER = config.tile_server  # e.g. "{region}/{z}/{x}/{y}.pbf"
COARSE_SEARCH_ZOOM = 9
DEEP_SEARCH_ZOOM = 12
TARGET_ZOOM = 15
CONCURRENCY_LIMIT = config.concurrency

INPUT_REGIONS_PATH = Path("data_raw/api/regions.json")
OUTPUT_Z15_PATH = Path("data_raw/validation_reports/Z15_tiles.json")

# ---------------------------------------------------------------------------
# Helpers – tile maths, HTTP, MVT parsing
# ---------------------------------------------------------------------------


def lonlat_to_tile(lon: float, lat: float, z: int) -> Tuple[int, int]:
    """Convert lon/lat to slippy‑map tile indices, clamped to [0, 2**z − 1]."""
    lat_rad = math.radians(lat)
    n = 2**z

    x_float = (lon + 180.0) / 360.0 * n
    y_float = (
        (1.0 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2.0 * n
    )

    xtile = int(min(n - 1, max(0, x_float)))
    ytile = int(min(n - 1, max(0, y_float)))
    return xtile, ytile


def has_parcels_with_geometry(tile_bytes: bytes) -> bool:
    """Return True if the MVT has at least one parcel feature with geometry."""
    from mapbox_vector_tile import decode
    import gzip

    try:
        if tile_bytes.startswith(b"\x1f\x8b"):
            tile_bytes = gzip.decompress(tile_bytes)
        data = decode(tile_bytes)
        parcels = data.get("parcels", {})
        if isinstance(parcels, dict):
            return any(bool(f.get("geometry")) for f in parcels.get("features", []))
    except Exception as exc:
        # Geometry/parsing errors are treated as permanent – no retry.
        logger.debug("MVT decode error", error=str(exc))
    return False


async def check_tile(
    client: httpx.AsyncClient, url: str, sem: asyncio.Semaphore
) -> bool:
    """Fetch a tile and decide whether it contains parcel geometry.

    Retries only on transient network/HTTP errors – not on decode failures."""

    transient = {429, 500, 502, 503, 504}
    for attempt in range(3):
        async with sem:
            try:
                resp = await client.get(url)
            except Exception as exc:
                logger.warning(
                    "Network error; retrying",
                    url=url,
                    error=str(exc),
                    attempt=attempt + 1,
                )
                await asyncio.sleep(2**attempt)
                continue

        if resp.status_code == 200:
            return has_parcels_with_geometry(resp.content)
        if resp.status_code == 404:
            return False
        if resp.status_code in transient:
            logger.warning(
                "Transient HTTP %s; retrying",
                resp.status_code,
                url=url,
                attempt=attempt + 1,
            )
            await asyncio.sleep(2**attempt)
            continue

        logger.warning("Permanent HTTP %s; skipping", resp.status_code, url=url)
        return False

    logger.error("Failed after retries", url=url)
    return False


# ---------------------------------------------------------------------------
# Discovery logic
# ---------------------------------------------------------------------------


def get_tiles_for_bbox(bbox: List[float], zoom: int) -> List[Tuple[int, int]]:
    min_lon, min_lat, max_lon, max_lat = bbox
    min_x, max_y = lonlat_to_tile(min_lon, min_lat, zoom)
    max_x, min_y = lonlat_to_tile(max_lon, max_lat, zoom)
    return [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]


async def gather_limited(coros, limit: int):
    """Run coroutines with a concurrency cap *and* bounded pending‑task count."""
    sem = asyncio.Semaphore(limit)
    results = []

    async def sem_wrapper(c):
        async with sem:
            return await c

    for coro in asyncio.as_completed([sem_wrapper(c) for c in coros]):
        results.append(await coro)
    return results


async def find_seed_tiles(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    region_slug: str,
    bbox: List[float],
) -> Set[Tuple[int, int]]:
    logger.info("[%s] Scanning z%d for seeds", region_slug, COARSE_SEARCH_ZOOM)
    coarse_tiles = get_tiles_for_bbox(bbox, COARSE_SEARCH_ZOOM)

    async def _check(t):
        x, y = t
        url = TILE_SERVER.format(region=region_slug, z=COARSE_SEARCH_ZOOM, x=x, y=y)
        return await check_tile(client, url, sem)

    has_data_flags = await gather_limited(map(_check, coarse_tiles), CONCURRENCY_LIMIT)

    factor = 2 ** (DEEP_SEARCH_ZOOM - COARSE_SEARCH_ZOOM)
    seeds = {
        (coarse_tiles[i][0] * factor, coarse_tiles[i][1] * factor)
        for i, flag in enumerate(has_data_flags)
        if flag
    }

    logger.info("[%s] Found %d seed tiles", region_slug, len(seeds))
    return seeds


async def discover_tiles_from_seeds(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    region_slug: str,
    seeds: Set[Tuple[int, int]],
) -> Set[Tuple[int, int]]:
    logger.info(
        "[%s] Flood‑fill at z%d from %d seed(s)",
        region_slug,
        DEEP_SEARCH_ZOOM,
        len(seeds),
    )

    queue: Set[Tuple[int, int]] = set(seeds)
    seen: Set[Tuple[int, int]] = set(seeds)  # Mark immediately to avoid duplication.
    tiles_with_data: Set[Tuple[int, int]] = set()

    async def _process(pt: Tuple[int, int]):
        x, y = pt
        url = TILE_SERVER.format(region=region_slug, z=DEEP_SEARCH_ZOOM, x=x, y=y)
        has_data = await check_tile(client, url, sem)
        return pt, has_data

    while queue:
        batch = list(queue)
        queue.clear()
        results = await gather_limited(map(_process, batch), CONCURRENCY_LIMIT)

        for (x, y), has_data in results:
            if has_data:
                tiles_with_data.add((x, y))
                # Enqueue 8‑neighbours.
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == dy == 0:
                            continue
                        nbr = (x + dx, y + dy)
                        if nbr not in seen:
                            seen.add(nbr)
                            queue.add(nbr)

    return tiles_with_data


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------


def expand_z12_to_z15(z12: Set[Tuple[str, int, int]]) -> List[dict]:
    """Generate z15 tile‑state rows from verified z12 tiles."""
    TILE_FACTOR = 2 ** (TARGET_ZOOM - DEEP_SEARCH_ZOOM)  # 8
    out: List[dict] = []
    for region, x12, y12 in z12:
        base_x = x12 * TILE_FACTOR
        base_y = y12 * TILE_FACTOR
        for dx in range(TILE_FACTOR):
            for dy in range(TILE_FACTOR):
                x15 = base_x + dx
                y15 = base_y + dy
                out.append(
                    {
                        "tile_id": f"{region}_{TARGET_ZOOM}_{x15}_{y15}",
                        "region": region,
                        "status": "pending",
                    }
                )
    return out


async def insert_z15_tiles_to_db(rows: List[dict]):
    if not rows:
        logger.info("No z15 tiles to insert")
        return

    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        total_inserted = 0
        BATCH = 1000
        for i in range(0, len(rows), BATCH):
            batch = rows[i : i + BATCH]
            try:
                result = await session.execute(
                    pg_insert(tile_state).on_conflict_do_nothing(
                        index_elements=[tile_state.c.tile_id]
                    ),
                    batch,
                )
                # rowcount may be -1 on some DBs; treat <0 as 0.
                total_inserted += max(0, result.rowcount or 0)
            except SQLAlchemyError as exc:
                logger.error("DB insert failed", error=str(exc))
                raise
        await session.commit()
        logger.info("Inserted %d new z15 rows", total_inserted)


# ---------------------------------------------------------------------------
# Region sourcing
# ---------------------------------------------------------------------------


async def get_regions_from_db():
    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        from scraper.db.models import regions

        stmt = (
            select(
                regions.c.region_name,
                regions.c.slug,
                regions.c.bounding_box_sw_x,
                regions.c.bounding_box_sw_y,
                regions.c.bounding_box_ne_x,
                regions.c.bounding_box_ne_y,
            )
            .where(
                regions.c.slug.isnot(None),
                regions.c.bounding_box_sw_x.isnot(None),
                regions.c.bounding_box_sw_y.isnot(None),
                regions.c.bounding_box_ne_x.isnot(None),
                regions.c.bounding_box_ne_y.isnot(None),
            )
            .order_by(regions.c.region_name)
        )

        res = await session.execute(stmt)
        return [
            {
                "slug": row.slug,
                "bbox": [
                    row.bounding_box_sw_x,
                    row.bounding_box_sw_y,
                    row.bounding_box_ne_x,  # east
                    row.bounding_box_ne_y,  # north
                ],
            }
            for row in res.mappings().all()
        ]


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------


async def main():
    logger.info("Tile‑discovery pipeline starting")

    # 1. Region catalogue ----------------------------------------------------
    try:
        regions = await get_regions_from_db()
        if not regions:
            raise RuntimeError("Empty region table")
    except Exception as exc:
        logger.warning("Falling back to static JSON", error=str(exc))
        if not INPUT_REGIONS_PATH.exists():
            logger.error("Region JSON missing at %s", INPUT_REGIONS_PATH)
            return
        with INPUT_REGIONS_PATH.open() as fh:
            data = json.load(fh).get("data", [])
        regions = [
            {
                "slug": r.get("mapStyleUrl", f"/{r['key']}").split("/")[-1],
                "bbox": r["bbox"],
            }
            for r in data
            if r.get("bbox")
        ]

    # 2. Discovery per region -----------------------------------------------
    verified_z12: Set[Tuple[str, int, int]] = set()
    sem = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async with httpx.AsyncClient(timeout=30) as client:
        for reg in regions:
            slug, bbox = reg["slug"], reg["bbox"]
            if not (slug and bbox):
                logger.warning("Skipping region with missing data", region=reg)
                continue

            seeds = await find_seed_tiles(client, sem, slug, bbox)
            if not seeds:
                logger.info("[%s] No data at z%d", slug, COARSE_SEARCH_ZOOM)
                continue

            filled = await discover_tiles_from_seeds(client, sem, slug, seeds)
            logger.info("[%s] Verified %d z12 tiles with data", slug, len(filled))
            verified_z12.update({(slug, x, y) for x, y in filled})

    # 3. Expand & persist ----------------------------------------------------
    if not verified_z12:
        logger.warning("No tiles discovered – exiting")
        return

    z15_rows = expand_z12_to_z15(verified_z12)
    await insert_z15_tiles_to_db(z15_rows)

    logger.info(
        "Tile‑discovery pipeline complete – %d z15 rows generated", len(z15_rows)
    )


if __name__ == "__main__":
    asyncio.run(main())
