import math
import asyncio
import httpx  # Replaces aiohttp
from mapbox_vector_tile import decode
from typing import List, Optional
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession
from scraper.db.engine import get_async_db_engine, get_async_session
from scraper.db.models import tile_state  # Use the actual Table object
from scraper.utils.config import get_discovery_config
import structlog
import gzip
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

BATCH_SIZE = 1000  # Insert in batches to avoid parameter limit errors

logger = structlog.get_logger()

config = get_discovery_config()
TILE_SERVER = config.tile_server
ZOOM10 = config.zoom10
ZOOM12 = config.zoom12
ZOOM15 = config.zoom15
MAX_RADIUS = 30
CONCURRENCY = config.concurrency


# --- Tile math ---
def lonlat_to_tile(lon: float, lat: float, z: int) -> tuple[int, int]:
    lat_rad = math.radians(lat)
    n = 2.0**z
    xtile = int((lon + 180.0) / 360.0 * n)
    ytile = int(
        (1.0 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2.0 * n
    )
    return xtile, ytile


# --- MVT parcel check ---
def has_parcels_with_geometry(tile_bytes: bytes) -> bool:
    try:
        # Decompress if gzipped
        if tile_bytes[:2] == b"\x1f\x8b":
            tile_bytes = gzip.decompress(tile_bytes)
        data = decode(tile_bytes)
        parcels = data.get("parcels", {})
        if isinstance(parcels, dict) and "features" in parcels:
            features = parcels["features"]
            return any(isinstance(f, dict) and f.get("geometry") for f in features)
    except Exception as e:
        print("Decode error:", e)
    return False


# --- Async HTTP fetch ---
async def fetch_and_check_tile(
    url: str, client: httpx.AsyncClient, sem: asyncio.Semaphore, max_retries: int = 3
) -> Optional[str]:
    for attempt in range(max_retries):
        async with sem:
            try:
                resp = await client.get(url)
                if resp.status_code == 200:
                    tile_bytes = resp.content
                    if has_parcels_with_geometry(tile_bytes):
                        return url
                    else:
                        logger.info("No parcels with geometry", url=url)
                        return None
                elif resp.status_code == 404:
                    logger.info("Tile not found (404)", url=url)
                    return None
                elif resp.status_code in (429, 500, 502, 503, 504):
                    logger.warn(
                        "Transient error, will retry",
                        url=url,
                        status=resp.status_code,
                        attempt=attempt + 1,
                    )
                    await asyncio.sleep(2**attempt)
                else:
                    logger.warn(
                        "Unexpected status code, not retrying",
                        url=url,
                        status=resp.status_code,
                    )
                    return None
            except Exception as e:
                logger.error(
                    "Network or decode error, will retry",
                    url=url,
                    error=str(e),
                    attempt=attempt + 1,
                )
                await asyncio.sleep(2**attempt)
    logger.error("Failed after retries", url=url)
    return None


# --- Discover z12 tiles with parcels ---
async def discover_z12_tiles(
    session: AsyncSession, regions: List[dict]
) -> List[tuple[str, int, int]]:
    z12_tiles_with_parcels = set()
    sem = asyncio.Semaphore(CONCURRENCY)
    async with httpx.AsyncClient(timeout=30) as client:
        tasks = []
        tile_coords = []
        for region in regions:
            region_slug = region["slug"]
            region_name = region["region_name"]
            centroid_x = region["centroid_x"]
            centroid_y = region["centroid_y"]
            if centroid_x is None or centroid_y is None or not region_slug:
                logger.warn(
                    "Skipping region with no centroid or slug",
                    region=region_name,
                )
                continue
            cx, cy = lonlat_to_tile(centroid_x, centroid_y, ZOOM10)
            first_url = None
            for dx in range(-MAX_RADIUS, MAX_RADIUS + 1):
                for dy in range(-MAX_RADIUS, MAX_RADIUS + 1):
                    x, y = cx + dx, cy + dy
                    url = TILE_SERVER.format(
                        region=region_slug,
                        z=ZOOM10,
                        x=x,
                        y=y,
                    )
                    if first_url is None:
                        first_url = url
                    tasks.append(fetch_and_check_tile(url, client, sem))
                    tile_coords.append((region_slug, x, y))
            logger.info(
                "Region and sample URL",
                region=region_name,
                slug=region_slug,
                sample_url=first_url,
            )
        results = await asyncio.gather(*tasks)
        z10_positive_coords = [tile_coords[i] for i, url in enumerate(results) if url]
        for region_slug, x10, y10 in z10_positive_coords:
            for dx in range(4):
                for dy in range(4):
                    x12 = x10 * 4 + dx
                    y12 = y10 * 4 + dy
                    z12_tiles_with_parcels.add((region_slug, x12, y12))
    return list(z12_tiles_with_parcels)


# --- Expand z12 to z15 tiles ---
def expand_z12_to_z15(z12_tiles: List[tuple[str, int, int]]) -> List[dict]:
    TILE_FACTOR = 8
    z15_tiles = []
    for region, x, y in z12_tiles:
        for dx in range(TILE_FACTOR):
            for dy in range(TILE_FACTOR):
                x15 = x * TILE_FACTOR + dx
                y15 = y * TILE_FACTOR + dy
                z15_tiles.append(
                    {
                        "tile_id": f"{region}_15_{x15}_{y15}",
                        "status": "pending",
                    }
                )
    return z15_tiles


# --- Insert into DB ---
async def insert_tiles(session: AsyncSession, tile_rows: List[dict]):
    if not tile_rows:
        return
    for i in range(0, len(tile_rows), BATCH_SIZE):
        batch = tile_rows[i : i + BATCH_SIZE]
        try:
            await session.execute(
                pg_insert(tile_state).on_conflict_do_nothing(
                    index_elements=[tile_state.c.tile_id]
                ),
                batch,
            )
        except SQLAlchemyError as e:
            logger.error("DB insert error", error=str(e), batch_size=len(batch))
            raise
    await session.commit()
    logger.info("Inserted z15 tile IDs into tile_state table", count=len(tile_rows))


# --- Fetch regions from DB ---
async def get_regions_with_centroids(session: AsyncSession):
    from scraper.db.models import regions

    stmt = select(
        regions.c.region_name,
        regions.c.slug,
        regions.c.centroid_x,
        regions.c.centroid_y,
    ).where(
        regions.c.centroid_x.isnot(None),
        regions.c.centroid_y.isnot(None),
        regions.c.slug.isnot(None),
    )
    result = await session.execute(stmt)
    return [
        {
            "region_name": row.region_name,
            "slug": row.slug,
            "centroid_x": row.centroid_x,
            "centroid_y": row.centroid_y,
        }
        for row in result.mappings().all()
    ]


# --- Main orchestration ---
async def run_discovery(output_json: Optional[str] = None):
    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        regions = await get_regions_with_centroids(session)
        z12_tiles = await discover_z12_tiles(session, regions)
        z15_tile_rows = expand_z12_to_z15(z12_tiles)
        await insert_tiles(session, z15_tile_rows)
        await session.commit()
        logger.info("Discovery phase complete", tile_count=len(z15_tile_rows))
