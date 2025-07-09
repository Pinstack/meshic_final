import typer
import asyncio
from scraper.pipelines.discovery import run_discovery
from scraper.utils.logging import setup_logging

app = typer.Typer(add_completion=False)


@app.command()
def discovery():
    """Run the discovery phase and insert discovered tile IDs into the database."""
    setup_logging()
    asyncio.run(run_discovery())


if __name__ == "__main__":
    app()
