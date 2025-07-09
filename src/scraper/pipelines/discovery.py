import math
import asyncio
import aiohttp
from mapbox_vector_tile import decode
from typing import List, Optional
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.scraper.db.engine import get_async_db_engine, get_async_session
from src.scraper.db.models import tile_state  # Use the actual Table object
from src.scraper.utils.config import get_discovery_config
import structlog
import json
import os
import gzip

logger = structlog.get_logger()

config = get_discovery_config()
TILE_SERVER = config["tile_server"]
ZOOM10 = config["zoom10"]
ZOOM12 = config["zoom12"]
ZOOM15 = config["zoom15"]
MAX_RADIUS = config["max_radius"]
CONCURRENCY = config["concurrency"]


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
    url: str, session: aiohttp.ClientSession, sem: asyncio.Semaphore
) -> Optional[str]:
    async with sem:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    tile_bytes = await resp.read()
                    if has_parcels_with_geometry(tile_bytes):
                        return url
        except Exception:
            pass
    return None


# --- Discover z12 tiles with parcels ---
# NOTE: This function now requires a list of region/centroid tuples, since Province ORM is not available.
async def discover_z12_tiles(
    session: AsyncSession, regions: List[dict]
) -> List[tuple[str, int, int]]:
    z12_tiles_with_parcels = set()
    sem = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as aio_session:
        tasks = []
        tile_coords = []
        for region in regions:
            region_name = region["region_name"]
            centroid_x = region["centroid_x"]
            centroid_y = region["centroid_y"]
            if centroid_x is None or centroid_y is None:
                logger.warn("Skipping region with no centroid", region=region_name)
                continue
            cx, cy = lonlat_to_tile(centroid_x, centroid_y, ZOOM10)
            for dx in range(-MAX_RADIUS, MAX_RADIUS + 1):
                for dy in range(-MAX_RADIUS, MAX_RADIUS + 1):
                    x, y = cx + dx, cy + dy
                    url = TILE_SERVER.format(
                        region=region_name,
                        z=ZOOM10,
                        x=x,
                        y=y,
                    )
                    tasks.append(fetch_and_check_tile(url, aio_session, sem))
                    tile_coords.append((region_name, x, y))
        results = await asyncio.gather(*tasks)
        z10_positive_coords = [tile_coords[i] for i, url in enumerate(results) if url]
        for region_name, x10, y10 in z10_positive_coords:
            for dx in range(4):
                for dy in range(4):
                    x12 = x10 * 4 + dx
                    y12 = y10 * 4 + dy
                    z12_tiles_with_parcels.add((region_name, x12, y12))
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
    stmt = pg_insert(tile_state).values(tile_rows)
    stmt = stmt.on_conflict_do_nothing(index_elements=["tile_id"])
    await session.execute(stmt)
    await session.commit()
    logger.info("Inserted z15 tile IDs into tile_state table", count=len(tile_rows))


# --- Optional: Write JSON output ---
def write_json(tile_ids: List[str], output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(tile_ids, f, ensure_ascii=False, indent=2)
    logger.info("Wrote z15 tile IDs to JSON", path=output_path, count=len(tile_ids))


# --- Main orchestration ---
async def run_discovery(output_json: Optional[str] = None):
    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        # TODO: Replace with actual region/centroid data source
        # For now, use a static example list
        regions = [
            {"region_name": "riyadh", "centroid_x": 46.6753, "centroid_y": 24.7136},
        ]
        z12_tiles = await discover_z12_tiles(session, regions)
        z15_tile_rows = expand_z12_to_z15(z12_tiles)
        await insert_tiles(session, z15_tile_rows)
        if output_json:
            write_json([row["tile_id"] for row in z15_tile_rows], output_json)
