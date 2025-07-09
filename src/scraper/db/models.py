from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    DateTime,
    Boolean,
    Index,
)
from sqlalchemy.dialects.postgresql import JSONB
from geoalchemy2 import Geometry

metadata = MetaData()

# Control table for tile state machine
tile_state = Table(
    "tile_state",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tile_id", String, unique=True, nullable=False),
    Column(
        "status", String, nullable=False
    ),  # e.g., pending, in_progress, done, failed
    Column("last_updated", DateTime),
    Column("error", String),
)

# Raw parcels staging table
parcels_raw = Table(
    "parcels_raw",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tile_id", String, nullable=False),
    Column("geometry", Geometry("MULTIPOLYGON", srid=4326, spatial_index=False)),
    Column("properties", JSONB),
    Column("ingested_at", DateTime),
    Index("app_parcels_raw_geometry_idx", "geometry", postgresql_using="gist"),
)

# Final stitched parcels table
parcels_final = Table(
    "parcels_final",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("geometry", Geometry("MULTIPOLYGON", srid=4326, spatial_index=False)),
    Column("h3_index", String),
    Column("attributes", JSONB),
    Column("enriched", Boolean, default=False),
    Column("updated_at", DateTime),
    Index("app_parcels_final_geometry_idx", "geometry", postgresql_using="gist"),
)
