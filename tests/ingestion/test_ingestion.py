from pathlib import Path

import httpx
import pytest

from scraper.pipelines import orchestrator

import shapely


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


def test_decode_empty_tile():
    tile_path = Path(__file__).parent.parent / "fixtures" / "empty_tile.pbf"
    if not tile_path.exists():
        pytest.skip("empty_tile.pbf missing")
    with tile_path.open("rb") as fh:
        data = fh.read()
    feats = orchestrator._decode_parcels(data)
    assert feats == []


def test_feature_to_row_valid():
    # Minimal valid GeoJSON polygon
    feature = {
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]],
        },
        "properties": {"foo": "bar"},
    }
    row = orchestrator._feature_to_row("tid", feature)
    assert row is not None
    assert isinstance(row["geometry"], bytes)
    # Check geometry is valid WKB
    geom = shapely.wkb.loads(row["geometry"])
    assert geom.is_valid
    assert row["properties"] == {"foo": "bar"}


def test_feature_to_row_invalid_geom():
    # Self-intersecting polygon (invalid)
    feature = {
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [0, 1], [1, 1], [0, 0]]],
        },
        "properties": {"bad": True},
    }
    row = orchestrator._feature_to_row("tid", feature)
    assert row is None


def test_feature_to_row_missing_geom():
    feature = {"properties": {"foo": "bar"}}
    row = orchestrator._feature_to_row("tid", feature)
    assert row is None


def test_partial_failure(monkeypatch):
    # One valid, one invalid feature
    valid = {
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]],
        },
        "properties": {"ok": 1},
    }
    invalid = {
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[0, 0], [1, 0], [0, 1], [1, 1], [0, 0]]],
        },
        "properties": {"bad": 1},
    }
    features = [valid, invalid]
    calls = []

    def fake_decode(_):
        return features

    monkeypatch.setattr(orchestrator, "_decode_parcels", fake_decode)

    class DummyDownloader:
        async def fetch_tile(self, z, x, y):
            return b""

    class DummySession:
        async def execute(self, *a, **k):
            calls.append((a, k))

        async def commit(self):
            pass

    async def fake_mark(session, tile_id, status, error=None):
        calls.append(("mark", status, error))

    monkeypatch.setattr(orchestrator, "_mark_tile", fake_mark)

    def fake_get_async_session(engine):
        class Ctx:
            async def __aenter__(self):
                return DummySession()

            async def __aexit__(self, *a):
                pass

        return Ctx()

    monkeypatch.setattr(orchestrator, "get_async_session", fake_get_async_session)
    row = {"tile_id": "t", "region": "r", "z": 15, "x": 1, "y": 2}
    import asyncio

    asyncio.run(orchestrator.ingest_one(object(), DummyDownloader(), row))
    # Only one insert (valid), one mark
    assert any("mark" in c for c in calls)


def test_logging_feature_error(monkeypatch, caplog):
    # Feature with missing geometry triggers error log
    import logging
    import structlog

    # Patch structlog to use standard logging for this test
    structlog.configure(
        processors=[
            structlog.processors.KeyValueRenderer(
                key_order=["event", "error", "tile_id"]
            )
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    feature = {"properties": {"foo": "bar"}}
    with caplog.at_level(logging.ERROR):
        orchestrator._feature_to_row("tid", feature)
    assert any("Feature decode error" in r.getMessage() for r in caplog.records)


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
