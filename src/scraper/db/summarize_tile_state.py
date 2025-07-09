import typer
from sqlalchemy import create_engine, text
from scraper.utils.config import get_discovery_config
from typing import Any, Dict
import json
import math


# --- MVTDecoder class (simplified for local use) ---
class MVTDecoder:
    INTEGER_ID_FIELDS = {
        "parcel_id",
        "zoning_id",
        "subdivision_id",
        "neighborhood_id",
        "province_id",
        "region_id",
    }
    STRING_ID_FIELDS = {
        "parcel_objectid",
        "rule_id",
        "station_code",
        "grid_id",
        "strip_id",
    }

    def _cast_property_types(self, properties: Dict[str, Any]) -> Dict[str, Any]:
        cast_properties = {}
        for key, value in properties.items():
            try:
                if key in self.INTEGER_ID_FIELDS:
                    if isinstance(value, int):
                        cast_properties[key] = value
                    elif isinstance(value, float):
                        cast_properties[key] = (
                            int(value) if value.is_integer() else None
                        )
                    elif isinstance(value, str):
                        try:
                            fval = float(value)
                            cast_properties[key] = (
                                int(fval) if fval.is_integer() else None
                            )
                        except Exception:
                            cast_properties[key] = None
                    else:
                        cast_properties[key] = None
                elif key in self.STRING_ID_FIELDS:
                    cast_properties[key] = str(value)
                else:
                    cast_properties[key] = value
            except Exception:
                cast_properties[key] = None
        return cast_properties

    def decode(self, tile_data: bytes) -> Dict[str, list]:
        import mapbox_vector_tile

        return mapbox_vector_tile.decode(tile_data)


def clean_json_for_postgres(obj):
    """Recursively replace NaN, inf, -inf with None in dicts/lists for JSONB compatibility."""
    if isinstance(obj, dict):
        return {k: clean_json_for_postgres(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_json_for_postgres(v) for v in obj]
    elif isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    else:
        return obj


app = typer.Typer()


def get_engine():
    config = get_discovery_config()
    engine = create_engine(config.database_url)
    return engine


@app.command()
def summarize_tile_state():
    """
    Summarizes the tile_state table: counts by status and a sample of tile IDs.
    """
    engine = get_engine()
    with engine.connect() as connection:
        # Count by status
        result = connection.execute(
            text("SELECT status, COUNT(*) FROM tile_state GROUP BY status")
        )
        typer.echo("--- tile_state counts by status ---")
        for status, count in result:
            typer.echo(f"  - {status}: {count}")

        # Show a sample of tile IDs
        sample = connection.execute(
            text("SELECT tile_id, status FROM tile_state LIMIT 10")
        )
        typer.echo("--- Sample tile_state rows ---")
        for row in sample:
            typer.echo(f"  - {row.tile_id}: {row.status}")


@app.command()
def summarize_parcels_raw():
    """
    Summarizes the parcels_raw table: row count, sample of tile_id/properties, geometry validity, and SRID.
    """
    engine = get_engine()
    with engine.connect() as connection:
        # Row count
        result = connection.execute(text("SELECT COUNT(*) FROM parcels_raw"))
        count = result.scalar()
        typer.echo(f"--- parcels_raw row count: {count} ---")

        # Sample rows
        sample = connection.execute(
            text("SELECT id, tile_id, ingested_at, properties FROM parcels_raw LIMIT 5")
        )
        typer.echo("--- Sample parcels_raw rows ---")
        for row in sample:
            typer.echo(
                f"  - id={row.id}, tile_id={row.tile_id}, ingested_at={row.ingested_at}, properties={str(row.properties)[:100]}"
            )

        # Geometry validity and SRID
        geom_check = connection.execute(
            text(
                "SELECT id, ST_IsValid(geometry) AS valid, ST_SRID(geometry) AS srid FROM parcels_raw LIMIT 5"
            )
        )
        typer.echo("--- Geometry validity and SRID ---")
        for row in geom_check:
            typer.echo(f"  - id={row.id}, valid={row.valid}, srid={row.srid}")


@app.command()
def ingest_local_pbf(
    pbf_path: str,
    tile_id: str = "local_test_tile",
):
    """
    Ingests a local .pbf file into parcels_raw using geopandas for decode/insert logic.
    """
    import geopandas as gpd

    engine = get_engine()
    from pathlib import Path
    import shapely
    import datetime

    pbf_path = Path(pbf_path)
    if not pbf_path.exists():
        typer.echo(f"File not found: {pbf_path}")
        raise typer.Exit(1)
    try:
        gdf = gpd.read_file(str(pbf_path), layer="parcels")
    except Exception as e:
        typer.echo(f"Failed to read with geopandas: {e}")
        raise typer.Exit(1)
    typer.echo(f"Layer 'parcels' has {len(gdf)} features.")
    features = []
    skipped = 0
    # Remove reprojection: keep geometries in native CRS (EPSG:3857)
    for i, row in gdf.iterrows():
        props = row.drop("geometry").to_dict()
        props = clean_json_for_postgres(props)
        geom = row.geometry
        # No reprojection here; keep as 3857
        if not isinstance(geom, shapely.geometry.base.BaseGeometry):
            skipped += 1
            typer.echo(f"Feature {i} skipped: geometry is not a shapely object.")
            continue
        if not geom.is_valid:
            geom = geom.buffer(0)
        if not geom.is_valid or geom.is_empty:
            skipped += 1
            typer.echo(f"Feature {i} skipped: invalid or empty geometry after repair.")
            continue
        wkb = geom.wkb
        features.append(
            {
                "tile_id": tile_id,
                "wkb": wkb,
                "properties": json.dumps(props),  # Ensure JSON serialization for JSONB
                "ingested_at": datetime.datetime.utcnow(),
            }
        )
    if not features:
        typer.echo("No valid features to insert.")
        return
    insert_stmt = text(
        """
        INSERT INTO parcels_raw (tile_id, geometry, properties, ingested_at)
        VALUES (:tile_id, ST_GeomFromWKB(:wkb, 3857), :properties, :ingested_at)
        """
    )
    with engine.connect() as connection:
        connection.execute(insert_stmt, features)
        connection.commit()
    typer.echo(
        f"Inserted {len(features)} features from {pbf_path}. "
        f"Skipped {skipped} invalid features."
    )


@app.command()
def inspect_pbf_geopandas(pbf_path: str):
    """
    Attempt to read a .pbf file with geopandas.read_file and print info/head.
    """
    import geopandas as gpd
    from pathlib import Path

    pbf_path = Path(pbf_path)
    if not pbf_path.exists():
        typer.echo(f"File not found: {pbf_path}")
        raise typer.Exit(1)
    try:
        gdf = gpd.read_file(str(pbf_path))
        typer.echo("geopandas.read_file succeeded.")
        typer.echo(gdf.info())
        typer.echo(gdf.head())
    except Exception as e:
        typer.echo(f"geopandas.read_file failed: {e}")


if __name__ == "__main__":
    app()
