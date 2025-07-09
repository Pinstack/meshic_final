import typer
from sqlalchemy import create_engine, text
from scraper.utils.config import get_discovery_config

app = typer.Typer()


def get_engine():
    config = get_discovery_config()
    engine = create_engine(config.database_url)
    return engine


@app.command()
def summarize_tile_state():
    """
    Summarizes the tile_state table: counts by status and a sample of tile IDs.
    """
    engine = get_engine()
    with engine.connect() as connection:
        # Count by status
        result = connection.execute(
            text("SELECT status, COUNT(*) FROM tile_state GROUP BY status")
        )
        typer.echo("--- tile_state counts by status ---")
        for status, count in result:
            typer.echo(f"  - {status}: {count}")

        # Show a sample of tile IDs
        sample = connection.execute(
            text("SELECT tile_id, status FROM tile_state LIMIT 10")
        )
        typer.echo("--- Sample tile_state rows ---")
        for row in sample:
            typer.echo(f"  - {row.tile_id}: {row.status}")


if __name__ == "__main__":
    app()
