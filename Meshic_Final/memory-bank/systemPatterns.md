# System Patterns

## Architecture Overview
- Modular pipeline: Each stage (discovery, ingestion, stitching, H3 indexing, enrichment) is a separate, idempotent module.
- Orchestrated via Typer CLI.
- Database-driven state machine: tile_state table tracks all work and status.
- Heavy spatial operations offloaded to PostGIS.

## Key Technical Decisions
- Use SQLAlchemy Core 2.0 (not ORM) for schema and bulk operations
- Use asyncpg for fast, async DB access
- Use httpx + asyncio for concurrent HTTP requests
- Use Alembic for migrations
- Use Pydantic for config
- Use structlog for logging

## Design Patterns
- Single Responsibility: Each module handles one stage
- Bulk Operations: COPY for ingestion, set-based SQL for stitching
- Resumable State: Status flags in DB, transactional updates

## Component Relationships
- CLI → Config → Pipeline Stage → DB Session → Models
- Logging at every step 