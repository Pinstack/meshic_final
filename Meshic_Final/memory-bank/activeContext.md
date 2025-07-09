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