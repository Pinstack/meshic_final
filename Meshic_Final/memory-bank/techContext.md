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