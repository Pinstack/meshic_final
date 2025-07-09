import pytest
import tempfile
from pathlib import Path
from scraper.utils.downloader import Downloader
import httpx
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_downloader_fetch_and_cache(monkeypatch):
    # Setup
    base_url = "https://tiles.example.com"
    z, x, y = 15, 1, 2
    tile_bytes = b"fake-tile-bytes"
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)

        # Patch httpx.AsyncClient.get to return a fake response
        async def fake_get(url, *args, **kwargs):
            class FakeResponse:
                status_code = 200
                content = tile_bytes

                def raise_for_status(self):
                    pass

            return FakeResponse()

        with patch("httpx.AsyncClient.get", new=AsyncMock(side_effect=fake_get)):
            async with Downloader(base_url, cache_dir) as dl:
                # First fetch: should call httpx and cache
                result = await dl.fetch_tile(z, x, y)
                assert result == tile_bytes
                # Second fetch: should use cache, not call httpx
                with patch(
                    "httpx.AsyncClient.get",
                    side_effect=Exception("Should not be called"),
                ):
                    result2 = await dl.fetch_tile(z, x, y)
                    assert result2 == tile_bytes


@pytest.mark.asyncio
async def test_downloader_404(monkeypatch):
    base_url = "https://tiles.example.com"
    z, x, y = 15, 1, 404
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)

        # Patch httpx.AsyncClient.get to return a 404
        async def fake_get(url, *args, **kwargs):
            class FakeResponse:
                status_code = 404
                content = b""

                def raise_for_status(self):
                    raise httpx.HTTPStatusError("404", request=None, response=self)

            return FakeResponse()

        with patch("httpx.AsyncClient.get", new=AsyncMock(side_effect=fake_get)):
            async with Downloader(base_url, cache_dir) as dl:
                result = await dl.fetch_tile(z, x, y)
                assert result is None
