from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    DateTime,
    Boolean,
    Index,
    Float,
)
from sqlalchemy.dialects.postgresql import JSONB
from geoalchemy2 import Geometry

JSONType = JSONB

metadata = MetaData()

# Control table for tile state machine
tile_state = Table(
    "tile_state",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tile_id", String, unique=True, nullable=True),
    Column("status", String, nullable=True),
    Column("last_updated", DateTime, nullable=True),
    Column("error", String, nullable=True),
)

# Raw parcels staging table
parcels_raw = Table(
    "parcels_raw",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("tile_id", String, nullable=True),
    Column(
        "geometry",
        Geometry("MULTIPOLYGON", srid=4326, spatial_index=False),
        nullable=True,
    ),
    Column("properties", JSONType, nullable=True),
    Column("ingested_at", DateTime, nullable=True),
    Index("app_parcels_raw_geometry_idx", "geometry", postgresql_using="gist"),
)

# Final stitched parcels table
parcels_final = Table(
    "parcels_final",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "geometry",
        Geometry("MULTIPOLYGON", srid=4326, spatial_index=False),
        nullable=True,
    ),
    Column("h3_index", String, nullable=True),
    Column("attributes", JSONType, nullable=True),
    Column("enriched", Boolean, default=False, nullable=True),
    Column("updated_at", DateTime, nullable=True),
    Index("app_parcels_final_geometry_idx", "geometry", postgresql_using="gist"),
)

# --- BEGIN: Extended DB Schema from schema_report.md ---

# Provinces table
provinces = Table(
    "provinces",
    metadata,
    Column("province_id", Integer, primary_key=True),
    Column("province_name", String, nullable=True),
    Column("centroid_x", Float, nullable=True),
    Column("centroid_y", Float, nullable=True),
)

# Regions table
regions = Table(
    "regions",
    metadata,
    Column("region_id", Integer, primary_key=True),
    Column("region_name", String, nullable=True),
    Column("province_id", Integer, nullable=True),  # FK to provinces
    Column("centroid_x", Float, nullable=True),
    Column("centroid_y", Float, nullable=True),
    Column("bounding_box_sw_x", Float, nullable=True),
    Column("bounding_box_sw_y", Float, nullable=True),
    Column("bounding_box_ne_x", Float, nullable=True),
    Column("bounding_box_ne_y", Float, nullable=True),
    Column("slug", String, nullable=True),  # Region slug for tile server URLs
)

# Neighborhoods table
# Neighborhood price metrics (e.g., price_of_meter)
# are computed from transactions of parcels in this neighborhood.
neighborhoods = Table(
    "neighborhoods",
    metadata,
    Column("neighborhood_id", Integer, primary_key=True),
    Column("neighborh_aname_ar", String, nullable=True),
    Column("neighborh_aname_en", String, nullable=True),
    Column("zoning_id", Integer, nullable=True),
    Column("zoning_color", String, nullable=True),
    Column("price_of_meter", String, nullable=True),
    Column("shape_area", String, nullable=True),
    Column("transaction_price", String, nullable=True),
    Column("region_id", Integer, nullable=True),  # FK to regions
    Column("province_id", Integer, nullable=True),  # FK to provinces
    Column(
        "geometry", Geometry("POLYGON", srid=4326, spatial_index=False), nullable=True
    ),
)

# Neighborhoods centroids table
neighborhoods_centroids = Table(
    "neighborhoods_centroids",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("neighborhood_id", Integer, nullable=True),
    Column("neighborh_aname_ar", String, nullable=True),
    Column("neighborh_aname_en", String, nullable=True),
    Column("province_id", Integer, nullable=True),
    Column(
        "geometry", Geometry("POINT", srid=4326, spatial_index=False), nullable=True
    ),
)

# Subdivisions table
subdivisions = Table(
    "subdivisions",
    metadata,
    Column("subdivision_id", Integer, primary_key=True),
    Column("subdivision_no", String, nullable=True),
    Column("zoning_id", Integer, nullable=True),
    Column("zoning_color", String, nullable=True),
    Column("transaction_price", String, nullable=True),
    Column("price_of_meter", String, nullable=True),
    Column("shape_area", String, nullable=True),
    Column("province_id", Integer, nullable=True),
    Column(
        "geometry",
        Geometry("MULTIPOLYGON", srid=4326, spatial_index=False),
        nullable=True,
    ),
)

# Parcels table (main)
# Each parcel may have multiple transactions
# (see transactions table, linked by parcel_objectid/parcel_id)
parcels = Table(
    "parcels",
    metadata,
    Column("parcel_objectid", String, primary_key=True),
    Column("province_id", Integer, nullable=True),
    Column("landuseagroup", String, nullable=True),
    Column("subdivision_no", String, nullable=True),
    Column("shape_area", String, nullable=True),
    Column("zoning_id", Integer, nullable=True),
    Column("neighborhaname_ar", String, nullable=True),
    Column("neighborhaname_en", String, nullable=True),
    Column("neighborhood_id", Integer, nullable=True),
    Column("municipality_aname_ar", String, nullable=True),
    Column("municipality_aname_en", String, nullable=True),
    Column("parcel_no", String, nullable=True),
    Column("subdivision_id", String, nullable=True),
    Column("transaction_price", String, nullable=True),
    Column("landuseadetailed", String, nullable=True),
    Column("parcel_id", Integer, nullable=True),
    Column("price_of_meter", String, nullable=True),
    Column("zoning_color", String, nullable=True),
    Column("ruleid", String, nullable=True),
    Column("block_no", String, nullable=True),
    Column(
        "geometry",
        Geometry("MULTIPOLYGON", srid=4326, spatial_index=False),
        nullable=True,
    ),
)

# Parcels base table
parcels_base = Table(
    "parcels_base",
    metadata,
    Column("parcel_objectid", String, primary_key=True),
    Column("province_id", Integer, nullable=True),
    Column("landuseagroup", String, nullable=True),
    Column("subdivision_no", String, nullable=True),
    Column("shape_area", String, nullable=True),
    Column("zoning_id", Integer, nullable=True),
    Column("neighborhaname_ar", String, nullable=True),
    Column("neighborhaname_en", String, nullable=True),
    Column("neighborhood_id", Integer, nullable=True),
    Column("municipality_aname_ar", String, nullable=True),
    Column("municipality_aname_en", String, nullable=True),
    Column("parcel_no", String, nullable=True),
    Column("subdivision_id", String, nullable=True),
    Column("transaction_price", String, nullable=True),
    Column("landuseadetailed", String, nullable=True),
    Column("parcel_id", Integer, nullable=True),
    Column("price_of_meter", String, nullable=True),
    Column("zoning_color", String, nullable=True),
    Column("ruleid", String, nullable=True),
    Column("block_no", String, nullable=True),
    Column(
        "geometry",
        Geometry("MULTIPOLYGON", srid=4326, spatial_index=False),
        nullable=True,
    ),
)

# Parcels centroids table
parcels_centroids = Table(
    "parcels_centroids",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("parcel_id", Integer),
    Column("parcel_no", String),
    Column("neighborhood_id", Integer),
    Column("province_id", Integer),
    Column("transactions_count", Integer),
    Column("transaction_date", String),
    Column("transaction_price", String),
    Column("price_of_meter", String),
    Column("geometry", Geometry("POINT", srid=4326, spatial_index=False)),
)

# Transactions table
# Each transaction is linked to a parcel and a neighborhood.
# Neighborhood price metrics are derived from these transactions.
transactions = Table(
    "transactions",
    metadata,
    Column("transaction_number", Integer, primary_key=True),
    Column("transaction_date", String),
    Column("transaction_price", String),
    Column("price_of_meter", String),
    Column("parcel_objectid", String),
    Column("parcel_id", Integer),
    Column("parcel_no", String),
    Column("block_no", String),
    Column("area", String),
    Column("zoning_id", Integer),
    Column("neighborhood_id", Integer),
    Column("region_id", Integer),
    Column("province_id", Integer),
    Column("subdivision_no", String),
    Column("subdivision_id", String),
    Column("centroid_x", String),
    Column("centroid_y", String),
    Column("metrics_type", String),
    Column("landuseagroup", String),
    Column("landuseadetailed", String),
    Column("geometry", Geometry("MULTIPOLYGON", srid=4326, spatial_index=False)),
)

# Parcel metrics priceOfMeter table
parcel_metrics_priceofmeter = Table(
    "parcel_metrics_priceofmeter",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("parcel_objid", String),
    Column("neighborhood_id", Integer),
    Column("month", Integer),
    Column("year", Integer),
    Column("metrics_type", String),
    Column("average_price_of_meter", String),
)

# Parcel building rules table
parcel_buildingrules = Table(
    "parcel_buildingrules",
    metadata,
    Column("id", String, primary_key=True),
    Column("zoning_id", Integer),
    Column("zoning_color", String),
    Column("zoning_group", String),
    Column("landuse", String),
    Column("description", String),
    Column("name", String),
    Column("coloring", String),
    Column("coloring_description", String),
    Column("max_building_coefficient", String),
    Column("max_building_height", String),
    Column("max_parcel_coverage", String),
    Column("max_rule_depth", String),
    Column("main_streets_setback", String),
    Column("secondary_streets_setback", String),
    Column("side_rear_setback", String),
)

# qi_population_metrics table
qi_population_metrics = Table(
    "qi_population_metrics",
    metadata,
    Column("grid_id", String, primary_key=True),
    Column("population_density", String),
    Column("residential_rpi", String),
    Column("commercial_rpi", String),
    Column("poi_count", String),
    Column("geometry", Geometry("POLYGON", srid=4326, spatial_index=False)),
)

# qi_stripes table
qi_stripes = Table(
    "qi_stripes",
    metadata,
    Column("strip_id", String, primary_key=True),
    Column("centroid_longitude", String),
    Column("centroid_latitude", String),
    Column("geometry", Geometry("POLYGON", srid=4326, spatial_index=False)),
)

# riyadh_bus_stations table
riyadh_bus_stations = Table(
    "riyadh_bus_stations",
    metadata,
    Column("station_code", String, primary_key=True),
    Column("station_name_ar", String),
    Column("station_name_en", String, nullable=True),
    Column("station_long", String),
    Column("station_lat", String),
    Column("geometry", Geometry("POINT", srid=4326, spatial_index=False)),
)

# bus_lines table
bus_lines = Table(
    "bus_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("originar_ar", String),
    Column("originar_en", String, nullable=True),
    Column("color", String),
    Column("type", String),
    Column("busroute", String),
    Column("origin", String),
    Column(
        "geometry",
        Geometry(
            "MULTILINESTRING",
            srid=4326,
            spatial_index=False,
        ),
    ),
)

# --- END: Extended DB Schema from schema_report.md ---

# Data quality caveats:
# - All geometry columns use WGS84 (EPSG:4326)
