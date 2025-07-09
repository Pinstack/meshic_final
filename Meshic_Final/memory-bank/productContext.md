# Product Context

## Why This Project Exists
Parcel data is fragmented across map tiles and lacks enrichment, making spatial analysis and downstream applications difficult. This project automates the extraction, enrichment, and consolidation of parcel polygons for reliable, queryable geospatial data.

## Problems Solved
- Eliminates manual tile management and data stitching
- Ensures data completeness and integrity
- Provides enriched, ready-to-use parcel data for analytics
- Enables fast spatial lookups via H3 indexing

## User Experience Goals
- Fully automated, resumable pipeline
- Clear CLI interface for all stages
- Transparent progress and error reporting
- Minimal manual intervention required 

---

**Pipeline Flexibility:**
- The pipeline is designed for maximum flexibility during data ingestion. Integrity checks and constraints (such as foreign keys) are applied only after data validation and cleaning.
- User experience goal: enable rapid iteration and robust analytics, with no data loss during schema evolution or pipeline changes. 