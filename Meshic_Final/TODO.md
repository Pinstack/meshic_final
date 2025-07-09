# Project TODO

## Phase 0: System & Database Setup
- [x] Install PostgreSQL 17.5 and PostGIS
- [x] Configure `shared_buffers = 4GB` in postgresql.conf for performance
- [x] Create database 'meshic_final' and user 'raedmundjennings'
- [x] Enable PostGIS extension
- [x] Test DB connection: postgresql://raedmundjennings@localhost:5432/meshic_final
- [x] Document the DB setup process for reproducibility (in README or separate doc)

## Phase 1: Project Scaffolding & Code Quality
- [x] Initialize git repository
- [x] Initialize Poetry and create virtual environment
- [x] Add core and dev dependencies via Poetry
- [x] Create .gitignore and .pre-commit-config.yaml for black, ruff, mypy
- [x] Run pre-commit install
- [x] Create folder structure: alembic/, configs/, src/scraper/db/, src/scraper/pipelines/, src/scraper/utils/, tests/
- [x] Add empty __init__.py files as needed
- [x] Initial commit

## Phase 2: Database Schema & Migrations
- [x] Define SQLAlchemy models for tile_state, parcels_raw, parcels_final in src/scraper/db/models.py
- [x] Initialize Alembic (alembic init alembic)
- [x] Edit alembic/env.py for async and metadata
- [x] Generate and review first migration
- [x] Apply migration to database

## Phase 2.5: Schema Refinement & Internationalization
- [x] Refactor all Arabic text columns to use _ar suffix and add corresponding _en columns (nullable)
- [x] Ensure all non-PK columns are nullable for flexibility
- [x] Document and enforce: Parcels have Transactions, Transactions enable Neighborhoods to derive price metrics, Parcels fetch those price metrics

## Phase 2.6: Git & Migration Workflow
- [x] Create feature branch for schema/i18n/nullability changes (e.g., feature/db-i18n-nullable)
- [x] Make small, focused commits for each logical change (Arabic/English columns, nullability, relationships, docs)
- [x] Generate and review Alembic migration script
- [x] Run all tests and validate migration on a test DB
- [x] Open a PR with a clear description of changes and next steps
- [x] Merge after review; rebase pipeline branch if needed
- [x] Tag the commit for reference (e.g., v0.2-schema-i18n)

## Phase 3: Ingestion (Modular)
- [x] Download and decode tiles, insert raw geometries (native CRS, e.g., EPSG:3857) into staging table (parcels_raw)
- [x] Reproject all geometries in staging table to EPSG:4326 using PostGIS (SQL), as a separate step/module
- [x] Document and test each stage for auditability and performance

## Phase 3.5: Geometry Processing & Reprojection
- [x] Perform all geometry operations (union, validation, deduplication) and reprojection in PostGIS using SQL (ST_Union, ST_Transform, etc.), not in Python
- [x] Insert geometries into staging/raw tables in their native CRS (typically EPSG:3857)
- [x] Reproject to EPSG:4326 in the DB after ingestion

## Phase 5: Visualization & Export
- [ ] After all DB processing, export data to GeoJSON for visualization (e.g., with Kepler.gl)
- [ ] Handle coordinate transformation for visualization at export time (not in Python pipeline)

## Phase 4: Orchestration & Finalization
- [ ] Build CLI in src/scraper/cli.py with Typer  # Use Z15 tiles for end-to-end local/manual pipeline runs
- [ ] Add commands for each stage and master command  # Use Z15 tiles for local/manual CLI command testing
- [ ] Add status command  # (Optional) Use Z15 tiles to check status reporting on real pipeline runs
- [ ] Implement config loading with Pydantic  # (Optional) Use Z15 tiles to validate config-driven runs
- [ ] Write unit and integration tests  # DO NOT use Z15 tiles for automated/CI tests; use only small fixtures in tests/fixtures/
- [ ] Write and update README.md  # (Optional) Document Z15 tile usage for local/manual testing 

# TODO

- [ ] Implement decode and feature extraction from .pbf tiles in the orchestrator
- [ ] Implement bulk insert of features into parcels_raw using SQLAlchemy Core
- [ ] Add robust error handling and status updates for each tile
- [ ] Expand tests for decode/insert logic (use fixtures in tests/fixtures/)
- [ ] Update documentation for decode/insert steps 

[x] Ensure all ingestion code paths use GeoPandas (GDAL/Fiona) for decoding .pbf files instead of mapbox-vector-tile, including orchestrator and any batch ingestion scripts.
[x] Double-check and enforce that all inserts into JSONB columns serialize dicts to JSON strings, or use the psycopg2 adapter, in all ingestion code paths.
[x] Validate and repair geometries using .buffer(0), and skip or log invalid/empty geometries in all ingestion logic.
[x] (Optional) Refactor for streaming and batch inserts for very large datasets using Fiona’s collection API and batch DB operations.

[ ] Implement PostGIS-based stitching, deduplication, and reprojection of ingested parcels for downstream analysis/export. 