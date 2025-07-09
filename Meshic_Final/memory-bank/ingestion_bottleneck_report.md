# Meshic Ingestion Pipeline: Bottleneck & Solution Report

## Project Goal
Ingest parcel features from Mapbox Vector Tile (.pbf) files into a PostGIS-backed staging table (`parcels_raw`). Each feature's geometry should be stored as WKB in a geometry column (native CRS, e.g., EPSG:3857), and all other properties as JSONB. The pipeline must be robust, auditable, and performant for large-scale, multi-region data.

---

## Pipeline Overview
1. **Discovery:** Identify which tiles contain parcel data and populate the `tile_state` table.
2. **Download & Decode:** Fetch .pbf tiles, decode features, extract geometry/properties.
3. **Insert:** Bulk insert features into `parcels_raw` (geometry as WKB, properties as JSONB).
4. **Reprojection & Transformation:** Downstream steps reproject and normalize data.

---

## Bottlenecks & Root Causes

### 1. Python Decoder Mismatch
- **Symptom:** `mapbox-vector-tile` (v2.1.0–2.2.0) failed to decode .pbf files, returning a list of strings instead of features.
- **Root Cause:** The Python library is not fully compatible with all MVT spec versions or encodings. Some tiles (especially those produced by modern/complex pipelines) are not parsed correctly.
- **Resolution:** Switched to `geopandas.read_file()` (GDAL/Fiona backend), which reliably reads .pbf vector tiles and yields valid features and geometries.

### 2. Database Insert Error (JSONB)
- **Symptom:** psycopg2/SQLAlchemy raised `ProgrammingError: can't adapt type 'dict'` when inserting feature properties as a Python dict into a JSONB column.
- **Root Cause:** psycopg2 cannot adapt Python dicts to PostgreSQL JSON/JSONB columns in raw SQL/text statements. The adapter works with ORM/Core insert objects, but not with `text()`.
- **Resolution:** Explicitly serialize the properties dict to a JSON string (`json.dumps(props)`) before insertion. PostgreSQL will store it as JSONB if the column type is correct.

---

## Key Lessons & Best Practices

- **Decoder Choice:** For robust, future-proof ingestion, prefer GDAL/Fiona (via GeoPandas) over pure-Python MVT decoders. This ensures compatibility with a wide range of vector tile formats and spec versions.
- **Data-Type Adaptation:** Always serialize Python dicts to JSON when writing to JSONB columns, unless using an ORM/Core insert that supports adapters.
- **Schema Alignment:** Use JSONB for semi-structured properties in PostgreSQL. This enables indexing, efficient queries, and flexible downstream processing.
- **Error Handling:** Log and skip invalid or empty geometries. Use `.buffer(0)` to attempt repair of invalid polygons.
- **Batch Inserts:** Use batch/transactional inserts for efficiency, but ensure all data types are DB-compatible.

---

## Recommendations for External Developers

1. **Use GeoPandas for Decoding:**
   - `gdf = geopandas.read_file(path_to_pbf, layer="parcels")`
   - Iterate over rows, extract geometry and properties.

2. **Prepare Data for Insert:**
   - Convert geometry to WKB: `geom.wkb`
   - Serialize properties: `json.dumps(props)`

3. **Insert into PostGIS:**
   - Use SQLAlchemy or psycopg2, but always pass properties as a JSON string for JSONB columns.
   - Example insert:
     ```python
     insert_stmt = text("""
         INSERT INTO parcels_raw (tile_id, geometry, properties, ingested_at)
         VALUES (:tile_id, ST_GeomFromWKB(:wkb, 3857), :properties, :ingested_at)
     """)
     # properties must be a JSON string
     ```

4. **Handle Geometry Validity:**
   - Use `shapely.is_valid` and `.buffer(0)` to repair invalid geometries.
   - Skip or log features that remain invalid or empty.

5. **Document and Log:**
   - Log all errors and skipped features for auditability.
   - Document all pipeline steps and known issues for future maintainers.

---

## References & Further Reading
- [GeoPandas read_file](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html)
- [psycopg2 JSON adaptation issue](https://github.com/psycopg/psycopg2/issues/796)
- [Mapbox Vector Tile Python library](https://pypi.org/project/mapbox-vector-tile/2.2.0/)

---

## Open Questions / Next Steps
- Should the pipeline support both GeoPandas and pure-Python decoders for maximum flexibility?
- Are there edge cases in tile encoding that require further compatibility testing?
- Should the ingestion pipeline support streaming/large-tile processing for memory efficiency?

---

**Contact:** For questions or to contribute improvements, please refer to the project maintainers or open an issue in the repository. 

---

## Targeted Validations & Proactive Enhancements (2024-07)

### 1. Decoder Mismatch
- **Validation:** mapbox-vector-tile v2.1.0–2.2.0 fails on some spec variants, returning strings instead of feature dicts [3].
- **Enhancement:** Consider integrating a C- or Rust-accelerated decoder (e.g., tilejson-vt, vtzero) as a fallback for performance and spec edge-cases.

### 2. GeoPandas Decoding
- **Validation:** geopandas.read_file(..., layer="parcels") via GDAL/Fiona is robust and future-proof [1].
- **Enhancement:** For large tiles, stream features using Fiona’s collection API (`with fiona.open(path) as collection: for feat in collection: ...`) to reduce memory pressure.

### 3. Database Insert Error (JSONB)
- **Validation:** psycopg2 raw-SQL/text inserts cannot adapt Python dicts—must use json.dumps(props) [2].
- **Enhancement:**
  - Register a global dict adapter:
    ```python
    from psycopg2.extras import register_adapter, Json
    register_adapter(dict, Json)
    ```
    (Works with ORM/Core, not raw text.)
  - For bulk inserts, use `psycopg2.extras.execute_values()` or PostgreSQL COPY for high throughput.

### 4. Geometry Handling
- **Validation:** .buffer(0) repair and skipping invalids is sound.
- **Enhancement:** Pre-validate with `shapely.prepared.prep()` and consider vectorized repairs via pygeos for speed.

---

### Additional Proactive Suggestions
- **Parallelism:** Use `concurrent.futures.ProcessPoolExecutor` or Dask to decode and prepare tiles in parallel.
- **Observability:** Emit metrics (e.g., count of skipped features, decode errors) to Prometheus or StatsD for monitoring.
- **Schema Optimizations:**
  - Add a GIN index on the properties JSONB column for fast property queries.
  - Include computed columns (e.g., tile_z, tile_x, tile_y) for partitioned storage and efficient querying.
- **Configurable Decoder Layer:** Abstract the decoder behind a factory pattern to allow runtime choice between GeoPandas, pure-Python, or C-based decoders.
- **Streaming Support:** For very large regions, integrate on-the-fly reprojection (e.g., via rasterio-style streams) to avoid double buffering.

---

**References**
[1] https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html
[2] https://github.com/psycopg/psycopg2/issues/796
[3] https://pypi.org/project/mapbox-vector-tile/2.2.0/ 