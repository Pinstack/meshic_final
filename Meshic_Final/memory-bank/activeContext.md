# Active Context

## Current Focus
- Database, PostGIS, and Alembic setup complete
- Schema and migrations are robust and in sync
- Ready to implement pipeline stages and CLI
- Config loader is now robust, type-safe, and fully tested using Pydantic. All pipeline code now uses attribute access for config values.

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