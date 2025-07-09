# Active Context

## Current Focus
- Database, PostGIS, and Alembic setup complete
- Schema and migrations are robust and in sync
- Ready to implement pipeline stages and CLI

## Recent Changes
- Database and PostGIS upgraded and configured
- Alembic async/sync config resolved for migrations
- Initial schema migration applied successfully

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