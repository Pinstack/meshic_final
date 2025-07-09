# Ingestion Pipeline: Developer Task List

## 1. Setup & Environment
- [ ] Install all dependencies using `requirements.txt` or Poetry.
- [ ] Set up a local database (Postgres or SQLite) using the provided schema-only SQL dump (`Reference_docs/meshic_final_schema.sql`).
- [ ] Ensure `configs/config.yaml` is present and correctly configured (especially `tile_server` and `database_url`).

## 2. Query Pending Tiles
- [ ] Query the `tile_state` table for all tiles with status `"pending"`.
  - Example SQL:
    ```sql
    SELECT tile_id, region, z, x, y FROM tile_state WHERE status = 'pending';
    ```

## 3. Download .pbf Tiles
- [ ] For each pending tile, construct the download URL using the pattern from `configs/config.yaml`:
    ```yaml
    tile_server: "https://tiles.suhail.ai/maps/{region}/{z}/{x}/{y}.vector.pbf"
    ```
- [ ] Download the .pbf file using an async HTTP client (e.g., httpx).

    **Python Example:**
    ```python
    import httpx

    tile_url = tile_server.format(region=region_slug, z=z, x=x, y=y)
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(tile_url)
        if resp.status_code == 200:
            tile_bytes = resp.content  # This is the .pbf file content
    ```

## 4. Decode .pbf and Extract Features
- [ ] Decode the .pbf file using `mapbox_vector_tile`.
- [ ] Extract parcel features from the `"parcels"` layer.

    **Python Example:**
    ```python
    from mapbox_vector_tile import decode

    data = decode(tile_bytes)
    parcels = data.get("parcels", {})
    features = parcels.get("features", [])
    ```

## 5. Insert Raw Geometries into Staging Table
- [ ] For each feature, prepare a row for insertion into the `parcels_raw` table.
  - Store the geometry in its native CRS (likely EPSG:3857).
  - Store any relevant properties/attributes.

    **Python Example:**
    ```python
    from sqlalchemy import insert

    rows = []
    for feature in features:
        rows.append({
            "tile_id": tile_id,
            "geometry": feature["geometry"],  # Convert to WKB/WKT as needed
            "properties": feature.get("properties", {}),
        })

    if rows:
        stmt = insert(parcels_raw).values(rows)
        await session.execute(stmt)
        await session.commit()
    ```

## 6. Update Tile Status
- [ ] After successful insertion, update the tile’s status in `tile_state` to `"ingested"`.
- [ ] If there is an error, update the status to `"failed"` and log the error.

## 7. Error Handling & Logging
- [ ] Log all download, decode, and DB errors.
- [ ] Optionally, archive failed .pbf files for debugging.

## 8. Testing
- [ ] Use provided test fixtures in `tests/fixtures/` for TDD.
- [ ] Write unit and integration tests for all steps.

## 9. Documentation
- [ ] Document any assumptions, edge cases, or questions.
- [ ] Update README or developer handoff docs as needed.

---

## Summary Table

| Step                | Tool/Lib/Pattern                | Output/Target                |
|---------------------|---------------------------------|------------------------------|
| Query pending tiles | SQLAlchemy/SQL                  | tile_state                   |
| Download .pbf       | httpx (async)                   | tile_bytes                   |
| Decode .pbf         | mapbox_vector_tile              | features (parcels layer)     |
| Insert to staging   | SQLAlchemy Core (insert)        | parcels_raw (native CRS)     |
| Update status       | SQLAlchemy Core (update)        | tile_state                   |
| Test & document     | pytest, fixtures, README        | -                            |

---

**Note:**
- The developer does not need access to the production DB. All work can be done with the provided schema and local test data/fixtures.
- The reprojection step is handled separately in PostGIS and is not part of this task. 