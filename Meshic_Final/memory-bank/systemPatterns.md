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

## Database Schema Patterns (2024-06)
- DB schema reverse-engineered from Riyadh z15 tile & API schema report (see Reference_docs/Schema/schema_report.md)
- All layers except streets and dimensions are mapped to SQLAlchemy Core tables
- PostGIS geometry types used for all spatial fields (WGS84/EPSG:4326)
- Cross-layer relationships (e.g., parcels, neighborhoods, subdivisions) are explicit; nullable FKs for known data quality issues
- All pipeline DB operations use SQLAlchemy Core, not ORM
- DB is the source of truth for region/province/neighborhood/parcel/subdivision data
- Sync logic will upsert region/province/neighborhood data from Suhail API 

## Config, Custom Scripts, and Data Mapping
- All pipeline config is defined in configs/config.yaml and loaded via src/scraper/utils/config.py (get_discovery_config()).
- Custom tile math, parcel detection, and async HTTP logic are implemented in src/scraper/pipelines/discovery.py.
- DB connection/session patterns are standardized in src/scraper/db/engine.py (get_async_db_engine, get_async_session).
- Canonical data mapping and field definitions are in Reference_docs/Schema/schema_report.md; example data in Reference_docs/*.json. 

## Data Relationships: Parcels, Transactions, Neighborhoods, Price Metrics

- **Parcels have Transactions:** Each parcel may have multiple transactions (sales, etc.), linked by `parcel_objectid`/`parcel_id`.
- **Transactions enable Neighborhoods to derive price metrics:** Neighborhood price metrics (e.g., `price_of_meter`) are computed from the transactions of parcels within that neighborhood.
- **Parcels fetch those price metrics:** Parcels reference price metrics derived from their neighborhood's transactions, ensuring up-to-date valuation and analytics.

These relationships are enforced in the schema (see models.py) and are critical for all downstream analytics and enrichment. 

---

## Staged Foreign Key Enforcement Pattern
- No foreign keys in staging/raw tables during initial ingestion and development.
- Data validation scripts are run to check for orphaned or invalid references before adding foreign keys.
- Foreign keys are added only to final/analytics tables via Alembic migration after data is robust.
- All pipeline logic uses SQLAlchemy Core (not ORM) for consistency and performance.
- Test-driven development: all schema changes are tested with static fixtures. 