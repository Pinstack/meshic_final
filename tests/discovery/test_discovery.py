import pytest
from src.scraper.pipelines import discovery
import os
import math


# --- Utility: tile indices to lon/lat (center of tile) ---
def tile_to_lonlat(x, y, z):
    n = 2.0**z
    lon = x / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
    lat = math.degrees(lat_rad)
    return lon, lat


# --- Real test for tile math (center-of-tile round-trip) ---
def test_tile_math_round_trip():
    # Reference: https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames
    # and MapTiler SDK JS wgs84ToTileIndex
    for x, y, z in [
        (512, 512, 10),
        (1205, 1540, 12),
        (20636, 14069, 15),
    ]:
        lon, lat = tile_to_lonlat(x + 0.5, y + 0.5, z)  # center of tile
        assert discovery.lonlat_to_tile(lon, lat, z) == (x, y)


# --- Test Riyadh tile math for known tile ---
def test_riyadh_tile_math():
    # Use the center of tile (20636, 14069) at zoom 15
    x, y, z = 20636, 14069, 15
    lon, lat = tile_to_lonlat(x + 0.5, y + 0.5, z)
    assert discovery.lonlat_to_tile(lon, lat, z) == (x, y)


# --- Real test for URL generation ---
def test_url_generation():
    url = discovery.TILE_SERVER.format(region="test", z=10, x=512, y=512)
    assert url == "https://tiles.suhail.ai/maps/test/10/512/512.vector.pbf"


# --- Real test for parcel geometry detection ---
def test_has_parcels_with_geometry():
    valid_tile_path = os.path.join(
        os.path.dirname(__file__), "../fixtures/valid_tile.pbf"
    )
    if os.path.exists(valid_tile_path):
        with open(valid_tile_path, "rb") as f:
            tile_bytes = f.read()
        assert discovery.has_parcels_with_geometry(tile_bytes) is True
    else:
        pytest.skip("valid_tile.pbf fixture not found")

    empty_tile_path = os.path.join(
        os.path.dirname(__file__), "../fixtures/empty_tile.pbf"
    )
    if os.path.exists(empty_tile_path):
        with open(empty_tile_path, "rb") as f:
            tile_bytes = f.read()
        assert discovery.has_parcels_with_geometry(tile_bytes) is False
    else:
        pytest.skip("empty_tile.pbf fixture not found")


# --- Test Riyadh parcel detection ---
def test_riyadh_parcel_detection():
    riyadh_tile_path = os.path.join(
        os.path.dirname(__file__), "../fixtures/riyadh_15_20636_14069.pbf"
    )
    if os.path.exists(riyadh_tile_path):
        with open(riyadh_tile_path, "rb") as f:
            tile_bytes = f.read()
        assert discovery.has_parcels_with_geometry(tile_bytes) is True
    else:
        pytest.skip("riyadh_15_20636_14069.pbf fixture not found")


# --- Test Riyadh parcel detection (new tile) ---
def test_riyadh_parcel_detection_20633_14065():
    tile_path = os.path.join(
        os.path.dirname(__file__), "../fixtures/riyadh_15_20633_14065.pbf"
    )
    if os.path.exists(tile_path):
        with open(tile_path, "rb") as f:
            tile_bytes = f.read()
        assert discovery.has_parcels_with_geometry(tile_bytes) is True
    else:
        pytest.skip("riyadh_15_20633_14065.pbf fixture not found")


def test_db_insertion(monkeypatch):
    # TODO: Use a mock AsyncSession and check insert_tiles logic
    pass


def test_end_to_end_discovery(monkeypatch):
    # TODO: Mock HTTP and DB, run run_discovery, check DB and (optional) JSON output
    pass
