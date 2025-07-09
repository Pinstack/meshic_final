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