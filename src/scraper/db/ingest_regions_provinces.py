import asyncio
import os
import httpx
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.dialects.postgresql import insert
from scraper.db.models import regions, provinces, metadata
import structlog

logger = structlog.get_logger()

DB_URL = os.environ.get(
    "DATABASE_URL", "postgresql+asyncpg://raedmundjennings@localhost:5432/meshic_final"
)
API_URL = os.environ.get(
    "REGIONS_API_URL", "https://tiles.suhail.ai/api/regions"
)  # Example endpoint


async def fetch_regions_from_api():
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(API_URL)
        resp.raise_for_status()
        return resp.json()["data"]


async def upsert_region_province(session, region_data):
    # Extract slug from mapStyleUrl
    map_style_url = region_data.get("mapStyleUrl", "")
    slug = map_style_url.rstrip("/").split("/")[-1] if map_style_url else None
    # Upsert provinces first
    for prov in region_data.get("provinces", []):
        prov_data = {
            "province_id": prov["id"],
            "province_name": prov["name"],
            "centroid_x": prov["centroid"]["x"] if prov.get("centroid") else None,
            "centroid_y": prov["centroid"]["y"] if prov.get("centroid") else None,
        }
        stmt = insert(provinces).values(**prov_data)
        stmt = stmt.on_conflict_do_update(
            index_elements=[provinces.c.province_id], set_=prov_data
        )
        await session.execute(stmt)
    # Upsert region
    region_row = {
        "region_id": region_data["id"],
        "region_name": region_data["key"],
        "centroid_x": (
            region_data["centroid"]["x"] if region_data.get("centroid") else None
        ),
        "centroid_y": (
            region_data["centroid"]["y"] if region_data.get("centroid") else None
        ),
        "bounding_box_sw_x": (
            region_data["restrictBoundaryBox"]["southwest"]["x"]
            if region_data.get("restrictBoundaryBox")
            else None
        ),
        "bounding_box_sw_y": (
            region_data["restrictBoundaryBox"]["southwest"]["y"]
            if region_data.get("restrictBoundaryBox")
            else None
        ),
        "bounding_box_ne_x": (
            region_data["restrictBoundaryBox"]["northeast"]["x"]
            if region_data.get("restrictBoundaryBox")
            else None
        ),
        "bounding_box_ne_y": (
            region_data["restrictBoundaryBox"]["northeast"]["y"]
            if region_data.get("restrictBoundaryBox")
            else None
        ),
        "slug": slug,
    }
    stmt = insert(regions).values(**region_row)
    stmt = stmt.on_conflict_do_update(
        index_elements=[regions.c.region_id], set_=region_row
    )
    await session.execute(stmt)


async def main():
    engine = create_async_engine(DB_URL, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    async with AsyncSession(engine) as session:
        data = await fetch_regions_from_api()
        for region in data:
            await upsert_region_province(session, region)
        await session.commit()
    logger.info("Regions and provinces ingested successfully from API.")

    # Verification: Log counts at INFO, details at DEBUG
    result = await session.execute(regions.select())
    region_rows = result.mappings().all()
    logger.info("Region count", count=len(region_rows))
    logger.debug("Region details", regions=[dict(row) for row in region_rows])
    result = await session.execute(provinces.select())
    province_rows = result.mappings().all()
    logger.info("Province count", count=len(province_rows))
    logger.debug("Province details", provinces=[dict(row) for row in province_rows])


if __name__ == "__main__":
    asyncio.run(main())
