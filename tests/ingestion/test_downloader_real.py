import pytest
from scraper.utils.downloader import Downloader
from scraper.db.engine import get_async_db_engine, get_async_session
from scraper.pipelines.orchestrator import get_pending_tiles
import os


@pytest.mark.integration
@pytest.mark.skipif(
    not os.environ.get("RUN_REAL_DOWNLOADER_TESTS"),
    reason="Set RUN_REAL_DOWNLOADER_TESTS=1 to run real downloader integration test.",
)
@pytest.mark.asyncio
async def test_downloader_real_batch():
    engine = get_async_db_engine()
    async with get_async_session(engine) as session:
        pending = await get_pending_tiles(session)
    if not pending:
        pytest.skip("No pending tiles in the database.")
    # Take a small batch (e.g., 3 tiles)
    batch = pending[:3]
    # Use config for base_url and cache_dir
    from scraper.utils.config import get_discovery_config

    config = get_discovery_config()
    # Use the full tile_server template and format with the first tile's region
    first_row = batch[0]
    base_url = config.tile_server.format(
        region=first_row["region"], z="{z}", x="{x}", y="{y}"
    )
    base_url = base_url.split("/{z}")[0]
    cache_dir = getattr(config, "tile_cache_dir", "data_raw/tile_cache")
    tiles = [(row["z"], row["x"], row["y"]) for row in batch]
    async with Downloader(base_url, cache_dir, concurrency=2) as dl:
        results = await dl.download_many(tiles)
    # Print results for manual inspection
    for tile, data in results.items():
        print(f"Tile {tile}: {len(data) if data else 'None'} bytes")
    # Assert at least one tile was downloaded (not None)
    assert any(data for data in results.values())
