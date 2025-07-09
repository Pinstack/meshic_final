# Progress

## What Works
- Database, PostGIS, and Alembic setup complete
- Initial schema migration applied successfully
- **Downloader and orchestrator pipeline are modular, robust, and fully tested.**

## What's Left to Build
- **Implement decode and DB insert steps for ingestion pipeline (decode .pbf, extract features, insert to staging table using SQLAlchemy Core).**
- **Add robust error handling and status updates for each tile.**
- **Write/expand tests and documentation for these steps.**
- Implement all pipeline stages (discovery, ingestion, stitching, H3 indexing, enrichment)
- Scaffold and implement Typer CLI
- Write tests and documentation

## Current Status
- Database and migrations are robust and ready for development
- **Downloader and orchestrator complete; next focus is decode/insert for ingestion.**

## Known Issues
- None 

## 2024-06-xx: Schema Alignment Progress
- DB schema now fully aligned with Riyadh z15 tile & API schema report (all layers except streets/dimensions)
- Outstanding:
  - Schema alignment tests
  - Region/province/neighborhood sync logic
  - Refactor discovery to use DB
  - Documentation and robust testing 

- Documentation and enforcement of the Parcels/Transactions/Neighborhoods/Price Metrics relationship is complete in both code and memory bank. 

---

**Progress Update:**
- Phase 2.5 (schema, nullability, _ar/_en conventions) is complete and tested.
- Current focus: staged foreign key enforcement and pipeline development.
- TODOs:
  - [ ] Continue pipeline development and data ingestion without foreign keys in staging/raw tables.
  - [ ] Implement data validation scripts for referential integrity.
  - [ ] Add foreign keys to final/analytics tables after validation.
  - [ ] Re-run validation and tests post-FK enforcement. 

- Geometry operations (union, validation, etc.) and reprojection are now handled in PostGIS using SQL (ST_Union, ST_Transform, etc.).
- New: After DB processing, export to GeoJSON for visualization (e.g., Kepler.gl). Coordinate transformation for visualization is handled at export time. 
- Ingestion and reprojection are now modular: download/decode to staging, then reproject in PostGIS.
- This improves auditability and performance. 

### 2024-07-09: Ingestion Complete
- Ingestion pipeline robust for batch .pbf ingestion (EPSG:3857).
- All test tiles ingested with 0 errors.
- DB schema (SRID 3857) and Alembic migration issues resolved.
- Next: PostGIS stitching, deduplication, reprojection. 