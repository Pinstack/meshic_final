# Tech Context

## Technologies Used
- Python 3.11+
- Poetry for dependency management
- PostgreSQL 15+ with PostGIS 3.4+ and postgis_h3
- SQLAlchemy Core 2.0
- asyncpg
- Alembic
- Typer
- Pydantic v2
- httpx
- mapbox-vector-tile
- shapely
- structlog

## Development Setup
- Use Poetry for virtualenv and dependencies
- Use pre-commit with black, ruff, mypy
- All code in src/, tests in tests/
- Config in configs/config.yaml

## Technical Constraints
- Must use async DB and HTTP libraries
- All spatial ops in PostGIS, not Python
- No ORM for bulk data
- All tests use static, version-controlled data 

## Config, Scripts, and Data Mapping (Onboarding)
- configs/config.yaml: All pipeline config (tile server, zooms, concurrency, etc.)
- src/scraper/utils/config.py: Loads config.yaml, provides get_discovery_config()
- src/scraper/pipelines/discovery.py: Custom tile math, parcel detection, async HTTP
- src/scraper/db/engine.py: DB engine/session helpers
- Reference_docs/Schema/schema_report.md: Canonical schema mapping
- Reference_docs/*.json: Example data for tests and onboarding 

---

**Tech Stack Updates:**
- Alembic is used for all schema migrations.
- SQLAlchemy Core is used for all pipeline logic (no ORM in main pipeline/data stages).
- Poetry manages dependencies and virtual environments.
- Database URL convention: `postgresql+asyncpg://raedmundjennings@localhost:5432/meshic_final` (set via `DATABASE_URL`).
- All DB operations use async engines for performance and scalability. 