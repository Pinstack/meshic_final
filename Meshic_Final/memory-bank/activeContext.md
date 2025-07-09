# Active Context

## Current Focus
- Database, PostGIS, and Alembic setup complete
- Schema and migrations are robust and in sync
- Ready to implement pipeline stages and CLI
- Config loader is now robust, type-safe, and fully tested using Pydantic. All pipeline code now uses attribute access for config values.
- **Downloader and orchestrator are modular, robust, and fully tested.**
- **Next immediate focus: Implement decode and DB insert steps for ingestion pipeline.**
- **Decode .pbf tiles, extract features, and insert into staging table using SQLAlchemy Core.**
- **Add robust error handling and status updates for each tile.**
- **Write/expand tests and documentation for these steps.**

## Recent Changes
- Database and PostGIS upgraded and configured
- Alembic async/sync config resolved for migrations
- Initial schema migration applied successfully
- Refactored config loading to use Pydantic (pydantic-settings) for validation and type safety. All config is now validated at load time, with robust defaults and error handling. Tests for config loading and validation are passing.

## Next Steps
- Implement pipeline stages (discovery, ingestion, stitching, H3 indexing, enrichment)
- Scaffold Typer CLI
- Begin TDD for each stage

## Active Decisions
- Use sync engine for Alembic, async for app
- Exclude PostGIS system tables from migrations
- Use unique spatial index names to avoid conflicts 

## 2024-06-xx: Schema Alignment & Next Steps
- DB schema now matches Riyadh z15 tile & API schema report (all layers except streets/dimensions)
- All fields, types, and relationships mapped to SQLAlchemy Core tables
- Next steps:
  1. Add schema alignment tests to ensure DB matches tile/API schema
  2. Implement sync logic to upsert region/province/neighborhood data from Suhail API
  3. Refactor discovery pipeline to use DB as source of truth
  4. Document and test all changes 

- The enforced relationships between Parcels, Transactions, Neighborhoods, and Price Metrics are now fully documented in both the schema (models.py) and the memory bank. This is a core data flow for the pipeline and is now explicit for all future development and review. 

---

**Current Focus (Post-Phase 2.5):**
- Phase 2.5 is complete: schema, nullability, and _ar/_en conventions are robust and tested.
- Current focus: pipeline development, data ingestion, and staged referential integrity enforcement.
- Next TODOs:
  - [ ] Continue pipeline development and data ingestion without foreign keys in staging/raw tables for maximum flexibility.
  - [ ] Implement data validation scripts to check for orphaned or invalid references before adding foreign keys.
  - [ ] Once pipeline and data are robust, add foreign keys to final/analytics tables via Alembic migration.
  - [ ] Re-run validation and tests to ensure referential integrity is enforced and no data is lost. 

---

**Local Data for Testing:**
- `Reference_docs/Z15_tiles/` is now documented as a local-only, gitignored archive of all province .pbf tiles for pipeline and DB validation.
- Use for local/manual testing and exploration; not required for CI/CD or automated tests. 

- Pipeline now inserts geometries into the staging/raw table in their native CRS (typically EPSG:3857 from the tile server).
- All reprojection to EPSG:4326 and geometry operations (union, validation, etc.) are performed in PostGIS using SQL (ST_Transform, ST_Union, etc.).
- For visualization (e.g., with Kepler.gl), export data as GeoJSON from the DB after all processing and reprojection are complete. Coordinate transformation for visualization is handled at export time. 

- The ingestion pipeline is now modularized:
  1. Download and decode tiles, insert raw geometries (native CRS) into staging table.
  2. Reproject all geometries in PostGIS as a separate step/module.
- This approach improves auditability, performance, and separation of concerns. 

- **Ingestion pipeline decision (2024-06):**
    - Geometry will be stored as WKB in a PostGIS `geometry` column (native CRS, e.g., EPSG:3857) in the staging table (`parcels_raw`).
    - All other feature properties will be stored as JSONB in a `properties` column.
    - Rationale: This approach maximizes spatial query performance, leverages PostGIS indexing, and maintains flexibility/auditability for raw data. It aligns with the modular, audit-first pipeline pattern and systemPatterns.md. 

---

**Ingestion Pipeline Optimizations (2024-06):**
- Use batch/transactional inserts (e.g., 500–1000 features per batch) for DB efficiency.
- Explicitly set SRID (e.g., 3857) on geometry column to ensure correct spatial reference in PostGIS.
- Validate geometries with `shapely.is_valid` before insert; log or skip invalid features.
- Log errors at both tile and feature level for traceability of partial failures.
- Ensure GIST index on geometry column and index on tile_id for fast queries.
- For very large tiles, process features in a streaming fashion to minimize memory usage.
- For extremely large ingests, consider Postgres COPY for bulk loading (advanced). 

## 2024-07-09: Ingestion Pipeline Update
- Ingestion pipeline now robustly ingests .pbf tiles in native EPSG:3857 using GeoPandas (GDAL/Fiona backend).
- All geometry validation, JSONB serialization, and DB schema (SRID 3857) issues resolved.
- Batch ingestion tested: all test tiles ingested with 0 errors/skips.
- Alembic migrations merged and version table supports long revision IDs.
- Ready for large-scale or automated batch ingestion.
- **Next step:** PostGIS-based stitching, deduplication, and reprojection pipeline. 