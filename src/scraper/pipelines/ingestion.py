"""Tile ingestion pipeline."""

from __future__ import annotations

import asyncio
import gzip
from datetime import datetime
from typing import List, Optional

import httpx
import structlog
from mapbox_vector_tile import decode
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from scraper.db.engine import get_async_db_engine, get_async_session
from scraper.db.models import parcels_raw, tile_state
from scraper.utils.config import get_discovery_config


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


async def ingest_one(
    session: AsyncSession, client: httpx.AsyncClient, row: dict
) -> None:
    config = get_discovery_config()
    url = config.tile_server.format(
        region=row["region"], z=row["z"], x=row["x"], y=row["y"]
    )
    try:
        resp = await client.get(url)
        resp.raise_for_status()
        features = _decode_parcels(resp.content)
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
    except Exception as exc:  # pragma: no cover - network/DB errors
        logger.error("Tile ingestion failed", tile_id=row["tile_id"], error=str(exc))
        await _mark_tile(session, row["tile_id"], "failed", str(exc))


async def run_ingestion(concurrency: int = 5) -> None:
    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        pending = await get_pending_tiles(session)
        if not pending:
            logger.info("No pending tiles found")
            return

        sem = asyncio.Semaphore(concurrency)
        async with httpx.AsyncClient(timeout=30) as client:
            tasks = []
            for row in pending:

                async def _worker(r=row):
                    async with sem:
                        await ingest_one(session, client, r)

                tasks.append(asyncio.create_task(_worker()))

            for t in asyncio.as_completed(tasks):
                await t
        await session.commit()
