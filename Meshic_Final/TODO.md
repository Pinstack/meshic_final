# Project TODO

## Phase 0: System & Database Setup
- [x] Install PostgreSQL 17.5 and PostGIS
- [x] Configure `shared_buffers = 4GB` in postgresql.conf for performance
- [x] Create database 'meshic_final' and user 'raedmundjennings'
- [x] Enable PostGIS extension
- [x] Test DB connection: postgresql://raedmundjennings@localhost:5432/meshic_final
- [x] Document the DB setup process for reproducibility (in README or separate doc)

## Phase 1: Project Scaffolding & Code Quality
- [x] Initialize git repository
- [x] Initialize Poetry and create virtual environment
- [x] Add core and dev dependencies via Poetry
- [x] Create .gitignore and .pre-commit-config.yaml for black, ruff, mypy
- [x] Run pre-commit install
- [x] Create folder structure: alembic/, configs/, src/scraper/db/, src/scraper/pipelines/, src/scraper/utils/, tests/
- [x] Add empty __init__.py files as needed
- [x] Initial commit

## Phase 2: Database Schema & Migrations
- [x] Define SQLAlchemy models for tile_state, parcels_raw, parcels_final in src/scraper/db/models.py
- [x] Initialize Alembic (alembic init alembic)
- [x] Edit alembic/env.py for async and metadata
- [x] Generate and review first migration
- [x] Apply migration to database

## Phase 3: Implement Pipeline Stages
- [ ] Implement Discovery Stage (src/scraper/pipelines/discovery.py, CLI command)
- [ ] Implement Ingestion Stage (src/scraper/pipelines/ingestion.py)
- [ ] Implement Stitching Stage (src/scraper/pipelines/stitching.py)
- [ ] Implement H3 Indexing Stage (src/scraper/pipelines/h3_indexing.py)
- [ ] Implement Enrichment Stage (src/scraper/pipelines/enrichment.py)

## Phase 4: Orchestration & Finalization
- [ ] Build CLI in src/scraper/cli.py with Typer
- [ ] Add commands for each stage and master command
- [ ] Add status command
- [ ] Implement config loading with Pydantic
- [ ] Write unit and integration tests
- [ ] Write and update README.md 