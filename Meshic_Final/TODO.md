# Project TODO

## Phase 0: System & Database Setup
- [ ] Install PostgreSQL 15+ and PostGIS 3.4+
- [ ] Configure `shared_buffers = 4GB` in postgresql.conf for performance
- [ ] Create database 'parcel_db' and user 'scraper_user'
- [ ] Enable PostGIS and h3 extensions
- [ ] Test DB connection: postgresql+asyncpg://scraper_user:your_secure_password@localhost:5432/parcel_db
- [ ] Document the DB setup process for reproducibility (in README or separate doc)

## Phase 1: Project Scaffolding & Code Quality
- [ ] Create project directory 'geo-scraper' and initialize git
- [ ] Create `.gitignore` file
- [ ] Initialize Poetry and create virtual environment
- [ ] Add core and dev dependencies via Poetry
- [ ] Create `.pre-commit-config.yaml` for black, ruff, mypy
- [ ] Run `pre-commit install`
- [ ] Create folder structure: alembic/, configs/, src/scraper/db/, src/scraper/pipelines/, src/scraper/utils/, tests/
- [ ] Add empty `__init__.py` files as needed
- [ ] Set up VS Code settings and recommend extensions (Python, PostgreSQL)
- [ ] Verify pre-commit hooks are working
- [ ] Initial commit

## Phase 2: Database Schema & Migrations
- [ ] Define SQLAlchemy models for tile_state, parcels_raw, parcels_final in src/scraper/db/models.py
- [ ] Initialize Alembic (alembic init alembic)
- [ ] Edit alembic/env.py for async and metadata
- [ ] Generate and review first migration
- [ ] Apply migration to database
- [ ] Write migration documentation or a migration README
- [ ] Test the migration on a fresh database

## Phase 3: Implement Pipeline Stages (TDD)
- [ ] Write unit tests for each pipeline stage before implementation (TDD)
- [ ] Implement Discovery Stage (src/scraper/pipelines/discovery.py, CLI command)
- [ ] Implement Ingestion Stage (src/scraper/pipelines/ingestion.py)
- [ ] Implement Stitching Stage (src/scraper/pipelines/stitching.py)
- [ ] Implement H3 Indexing Stage (src/scraper/pipelines/h3_indexing.py)
- [ ] Implement Enrichment Stage (src/scraper/pipelines/enrichment.py)
- [ ] Document the API contract for the Suhail API
- [ ] Set up error handling and logging in each stage

## Phase 4: Orchestration & Finalization
- [ ] Build CLI in src/scraper/cli.py with Typer
- [ ] Add commands for each stage and master command
- [ ] Add status command
- [ ] Implement config loading with Pydantic
- [ ] Create example config files (e.g., config.yaml.example)
- [ ] Write unit and integration tests
- [ ] Set up continuous integration (CI) for automated testing
- [ ] Set up code coverage reporting
- [ ] Write and update README.md
- [ ] Add user/developer documentation beyond the README (if needed) 