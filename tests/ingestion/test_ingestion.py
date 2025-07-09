from pathlib import Path

import httpx
import pytest

from scraper.pipelines import orchestrator


def test_parse_tile_id():
    assert orchestrator._parse_tile_id("riyadh_15_1_2") == ("riyadh", 15, 1, 2)
    assert orchestrator._parse_tile_id("bad") is None


def test_decode_parcels():
    tile_path = Path(__file__).parent.parent / "fixtures" / "valid_tile.pbf"
    if not tile_path.exists():
        pytest.skip("valid_tile.pbf missing")
    with tile_path.open("rb") as fh:
        data = fh.read()
    feats = orchestrator._decode_parcels(data)
    assert isinstance(feats, list)
    assert feats


class DummySession:
    def __init__(self, ids):
        self.ids = ids

    async def execute(self, stmt, *args, **kwargs):
        class R:
            def scalars(self_inner):
                for tid in self.ids:
                    yield tid

        return R()


@pytest.mark.asyncio
async def test_get_pending_tiles():
    session = DummySession(["reg_15_1_2", "bad"])
    tiles = await orchestrator.get_pending_tiles(session)
    assert len(tiles) == 1
    assert tiles[0]["x"] == 1


class DummyResponse:
    def __init__(self, content=b"", status_code=200):
        self.content = content
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError("err", request=None, response=None)


class Recorder(DummySession):
    def __init__(self):
        super().__init__([])
        self.calls = []

    async def execute(self, stmt, params=None):
        self.calls.append((stmt, params))

    async def commit(self):
        pass


@pytest.mark.asyncio
async def test_ingest_one(monkeypatch):
    tile_path = Path(__file__).parent.parent / "fixtures" / "valid_tile.pbf"
    if not tile_path.exists():
        pytest.skip("valid_tile.pbf missing")
    tile_bytes = tile_path.read_bytes()

    class MockDownloader:
        async def fetch_tile(self, z, x, y):
            return tile_bytes

    downloader = MockDownloader()
    session = Recorder()

    async def fake_mark(session_, tile_id, status, error=None):
        session.calls.append(("mark", status))

    # Patch _mark_tile to avoid DB
    monkeypatch.setattr(orchestrator, "_mark_tile", fake_mark)

    # Patch get_async_session to return our Recorder
    def fake_get_async_session(engine):
        class DummyContext:
            async def __aenter__(self_inner):
                return session

            async def __aexit__(self_inner, exc_type, exc, tb):
                pass

        return DummyContext()

    monkeypatch.setattr(orchestrator, "get_async_session", fake_get_async_session)

    row = {"tile_id": "r_15_1_2", "region": "r", "z": 15, "x": 1, "y": 2}
    # Pass a dummy engine (not used)
    await orchestrator.ingest_one(object(), downloader, row)

    assert session.calls  # insert executed
    assert ("mark", "ingested") in session.calls
