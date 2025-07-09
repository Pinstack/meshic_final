import pytest
from sqlalchemy import insert, select
from scraper.db.engine import get_async_db_engine
from scraper.db import models

# List of tables and their PKs for nullability tests
TABLES = [
    (models.parcels, {"parcel_objectid": "test_parcel"}),
    (models.parcels_base, {"parcel_objectid": "test_parcel_base"}),
    (models.neighborhoods, {"neighborhood_id": 999999}),
    (models.neighborhoods_centroids, {"id": 999999}),
    (models.subdivisions, {"subdivision_id": 999999}),
    (models.provinces, {"province_id": 999999}),
    (models.regions, {"region_id": 999999}),
    (models.parcels_centroids, {"id": 999999}),
    (models.transactions, {"transaction_number": 999999}),
    (models.parcel_buildingrules, {"id": "test_rule"}),
    (models.parcel_metrics_priceofmeter, {"id": 999999}),
    (models.qi_population_metrics, {"grid_id": "test_grid"}),
    (models.qi_stripes, {"strip_id": "test_strip"}),
    (models.riyadh_bus_stations, {"station_code": "test_station"}),
    (models.bus_lines, {"id": 999999}),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("table, pk_dict", TABLES)
async def test_insert_with_only_pk(table, pk_dict):
    engine = get_async_db_engine()
    async with engine.begin() as conn:
        await conn.execute(insert(table).values(**pk_dict))
        result = await conn.execute(
            select(table).where(*[getattr(table.c, k) == v for k, v in pk_dict.items()])
        )
        row = result.first()
        assert row is not None
    await engine.dispose()


@pytest.mark.asyncio
async def test_ar_en_columns_independent_nullability():
    engine = get_async_db_engine()
    async with engine.begin() as conn:
        # Test parcels _ar/_en
        await conn.execute(
            insert(models.parcels).values(
                parcel_objectid="test_ar_en_1",
                neighborhaname_ar="حي الاختبار",
                neighborhaname_en=None,
            )
        )
        await conn.execute(
            insert(models.parcels).values(
                parcel_objectid="test_ar_en_2",
                neighborhaname_ar=None,
                neighborhaname_en="Test Neighborhood",
            )
        )
        # Test bus_lines _ar/_en
        await conn.execute(
            insert(models.bus_lines).values(
                id=888888, originar_ar="محطة اختبار", originar_en=None
            )
        )
        await conn.execute(
            insert(models.bus_lines).values(
                id=888889, originar_ar=None, originar_en="Test Station"
            )
        )
    await engine.dispose()
