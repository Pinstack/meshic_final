# Project Brief

## Project Goal
Build a fully automated, resilient Python pipeline that scrapes parcel polygons from a Mapbox Vector Tile (MVT) service, enriches them with data from a third-party API (Suhail API), and stores the final, clean data in a locally hosted PostgreSQL/PostGIS database.

## Core Requirements
- Modular, idempotent pipeline stages orchestrated via CLI
- Central database table tracks state of each task for resumability and fault tolerance
- Stages: Discovery, Ingestion, Stitching, H3 Indexing, Enrichment
- Database as a state machine (tile_urls table as source of truth)
- Performance-oriented: heavy spatial processing in PostGIS, efficient bulk-loading
- Modular, maintainable codebase with modern tooling
- All geometry operations (union, validation, deduplication) and reprojection are performed in PostGIS using SQL (ST_Union, ST_Transform, etc.), not in Python.
- Visualization (e.g., with Kepler.gl) is performed after exporting GeoJSON from the database, with coordinate transformation handled at export time.
- The pipeline is modular: (1) Download and decode tiles to staging table in native CRS; (2) Reproject all geometries in PostGIS as a separate step/module.
- This design improves auditability and leverages PostGIS for spatial operations and performance.

## Out of Scope
- Manual intervention in pipeline stages
- Non-PostgreSQL databases
- Non-automated enrichment processes 

---

**Update (Phase 2.5 Complete):**
- The staged approach to foreign keys is now the official policy: raw/staging tables remain flexible, and referential integrity is enforced only after validation and data quality checks.
- The schema and pipeline are robust, with all nullability and _ar/_en conventions enforced and tested. 