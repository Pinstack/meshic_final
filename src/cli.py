import typer
import asyncio
from src.scraper.pipelines.discovery import run_discovery

app = typer.Typer()


@app.command()
def discovery(
    output_json: str = typer.Option(
        None, help="Optional path to write discovered z15 tile URLs as JSON"
    )
):
    """Discover z15 tiles with parcels and populate the database."""
    asyncio.run(run_discovery(output_json=output_json))


if __name__ == "__main__":
    app()
