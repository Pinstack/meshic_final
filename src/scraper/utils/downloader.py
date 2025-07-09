import asyncio
import httpx
from pathlib import Path
import logging
from typing import Optional, Tuple, Dict, List
import datetime

logger = logging.getLogger(__name__)


class Downloader:
    def __init__(
        self,
        base_url: str,
        cache_dir: str | Path,
        concurrency: int = 5,
        max_retries: int = 3,
        request_timeout: float = 30.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.cache_dir = Path(cache_dir)
        self.concurrency = concurrency
        self.max_retries = max_retries
        self.request_timeout = request_timeout
        self.semaphore = asyncio.Semaphore(concurrency)
        self.client: Optional[httpx.AsyncClient] = None
        self.failed_log_path = self.cache_dir / "failed_downloads.log"

    async def __aenter__(self):
        self.client = httpx.AsyncClient(timeout=self.request_timeout)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.client:
            await self.client.aclose()

    def get_tile_cache_path(self, z: int, x: int, y: int) -> Path:
        tile_dir = self.cache_dir / str(z) / str(x)
        tile_dir.mkdir(parents=True, exist_ok=True)
        return tile_dir / f"{y}.pbf"

    async def fetch_tile(self, z: int, x: int, y: int) -> Optional[bytes]:
        cache_path = self.get_tile_cache_path(z, x, y)
        if cache_path.exists():
            logger.debug(f"Tile {z}/{x}/{y} found in cache.")
            return cache_path.read_bytes()
        url = f"{self.base_url}/{z}/{x}/{y}.vector.pbf"
        async with self.semaphore:
            for attempt in range(self.max_retries):
                resp = None
                try:
                    resp = await self.client.get(url)
                    if resp.status_code == 404:
                        logger.warning(f"Tile {z}/{x}/{y} not found (404). Skipping.")
                        return None
                    resp.raise_for_status()
                    # httpx should handle decompression automatically
                    cache_path.write_bytes(resp.content)
                    return resp.content
                except httpx.HTTPStatusError as e:
                    if e.response.status_code == 404:
                        logger.warning(f"Tile {z}/{x}/{y} not found (404). Skipping.")
                        return None
                    logger.warning(f"HTTP error for tile {z}/{x}/{y}: {e}. Retrying...")
                    self._log_failed_download(z, x, y, str(e), attempt + 1)
                except Exception as e:
                    if resp is not None:
                        headers = getattr(resp, "headers", None)
                        content = (
                            getattr(resp, "content", b"")[:16]
                            if hasattr(resp, "content") and resp.content is not None
                            else b""
                        )
                        logger.warning(
                            f"Error downloading tile {z}/{x}/{y}: {e}. Retrying..."
                        )
                        logger.warning(f"Headers: {headers}")
                        logger.warning("First 16 bytes: %r", content)
                    else:
                        logger.warning(
                            f"Error downloading tile {z}/{x}/{y}: {e}. Retrying..."
                        )
                    self._log_failed_download(z, x, y, str(e), attempt + 1)
                await asyncio.sleep(2**attempt)
            logger.error(
                f"Failed to download tile {z}/{x}/{y} after "
                f"{self.max_retries} attempts."
            )
            self._log_failed_download(z, x, y, "Max retries exceeded", self.max_retries)
            return None

    def _log_failed_download(self, z, x, y, error, attempt):
        self.failed_log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.failed_log_path, "a") as f:
            f.write(
                f"{datetime.datetime.utcnow().isoformat()} | z={z} x={x} y={y} | attempt={attempt} | error={error}\n"
            )

    async def download_many(
        self, tiles: List[Tuple[int, int, int]]
    ) -> Dict[Tuple[int, int, int], Optional[bytes]]:
        results: Dict[Tuple[int, int, int], Optional[bytes]] = {}

        async def fetch_and_store(tile):
            z, x, y = tile
            results[tile] = await self.fetch_tile(z, x, y)

        await asyncio.gather(*(fetch_and_store(tile) for tile in tiles))
        return results
