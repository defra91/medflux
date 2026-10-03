# src/medflux/cli.py

from pathlib import Path

import click

from .main import main


@click.command()
@click.option(
    "--db-path", "-d", required=True, type=click.Path(exists=True, dir_okay=False), help="Path to the database file"
)
@click.option("--output-path", "-o", required=True, type=click.Path(dir_okay=False), help="Path to the output pdf file")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--debug", "-g", is_flag=True, help="Enable debug mode")
def cli(db_path: str, output_path: str, verbose: bool, debug: bool):

    db_path = Path(db_path)
    output_path = Path(output_path)

    main(db_path, output_path, verbose, debug)
