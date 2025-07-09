"""Tile orchestration pipeline."""

from __future__ import annotations

import asyncio
import gzip
from datetime import datetime
from typing import List, Optional

import structlog
from mapbox_vector_tile import decode
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from scraper.db.engine import get_async_db_engine, get_async_session
from scraper.db.models import parcels_raw, tile_state
from scraper.utils.config import get_discovery_config
from scraper.utils.downloader import Downloader


logger = structlog.get_logger()


def _parse_tile_id(tile_id: str) -> Optional[tuple[str, int, int, int]]:
    """Parse ``region,z,x,y`` from a tile_id string."""

    try:
        region, z, x, y = tile_id.split("_")
        return region, int(z), int(x), int(y)
    except Exception:
        logger.warning("Invalid tile_id", tile_id=tile_id)
        return None


async def get_pending_tiles(session: AsyncSession) -> List[dict]:
    """Fetch pending tiles with parsed coordinates."""

    stmt = select(tile_state.c.tile_id).where(tile_state.c.status == "pending")
    result = await session.execute(stmt)
    tiles: List[dict] = []
    for tid in result.scalars():
        parsed = _parse_tile_id(tid)
        if parsed:
            region, z, x, y = parsed
            tiles.append({"tile_id": tid, "region": region, "z": z, "x": x, "y": y})
    return tiles


def _decode_parcels(tile_bytes: bytes) -> List[dict]:
    if tile_bytes[:2] == b"\x1f\x8b":
        tile_bytes = gzip.decompress(tile_bytes)
    data = decode(tile_bytes)
    parcels = data.get("parcels", {})
    return parcels.get("features", []) if isinstance(parcels, dict) else []


async def _mark_tile(
    session: AsyncSession, tile_id: str, status: str, error: Optional[str] = None
) -> None:
    await session.execute(
        update(tile_state)
        .where(tile_state.c.tile_id == tile_id)
        .values(status=status, error=error, last_updated=datetime.utcnow())
    )


async def ingest_one(engine, downloader: Downloader, row: dict) -> None:
    get_discovery_config()
    async with get_async_session(engine) as session:
        try:
            tile_bytes = await downloader.fetch_tile(row["z"], row["x"], row["y"])
            if not tile_bytes:
                raise ValueError(f"Failed to download tile for {row}")
            features = _decode_parcels(tile_bytes)
            if features:
                rows = [
                    {
                        "tile_id": row["tile_id"],
                        "geometry": f["geometry"],
                        "properties": f.get("properties", {}),
                        "ingested_at": datetime.utcnow(),
                    }
                    for f in features
                ]
                await session.execute(insert(parcels_raw), rows)
            await _mark_tile(session, row["tile_id"], "ingested")
            await session.commit()
        except Exception as exc:  # pragma: no cover - network/DB errors
            logger.error(
                "Tile orchestration failed", tile_id=row["tile_id"], error=str(exc)
            )
            await _mark_tile(session, row["tile_id"], "failed", str(exc))
            await session.commit()


async def run_orchestration(concurrency: int = 5) -> None:
    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        pending = await get_pending_tiles(session)
    if not pending:
        logger.info("No pending tiles found")
        return

    # Filter out invalid tile IDs
    valid_pending = []
    for row in pending:
        if _parse_tile_id(row["tile_id"]):
            valid_pending.append(row)
        else:
            logger.warning("Skipping invalid tile_id", tile_id=row["tile_id"])

    if not valid_pending:
        logger.info("No valid pending tiles found")
        return

    sem = asyncio.Semaphore(concurrency)
    config = get_discovery_config()
    base_url = config.tile_server.split("/{z}")[0]
    cache_dir = getattr(config, "tile_cache_dir", "data_raw/tile_cache")
    async with Downloader(base_url, cache_dir, concurrency=concurrency) as downloader:
        tasks = []
        for row in valid_pending:

            async def _worker(r=row):
                async with sem:
                    await ingest_one(engine, downloader, r)

            tasks.append(asyncio.create_task(_worker()))
        for t in asyncio.as_completed(tasks):
            await t
