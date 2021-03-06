"""Command line interface of aldernet."""
# Standard library
import logging

# Third-party
import click

# Local
from . import __version__
from .utils import count_to_log_level


@click.command()
@click.option(
    "--dry-run",
    "-n",
    flag_value="dry_run",
    default=False,
    help="Perform a trial run with no changes made",
)
@click.option(
    "--verbose",
    "-v",
    count=True,
    help="Increase verbosity (specify multiple times for more)",
)
@click.option(
    "--version",
    "-V",
    is_flag=True,
    help="Print version",
)
def main(*, dry_run: bool, verbose: int, version: bool) -> None:
    logging.basicConfig(level=count_to_log_level(verbose))

    logging.warning("This is a warning.")
    logging.info("This is an info message.")
    logging.debug("This is a debug message.")

    if version:
        click.echo(__version__)
        return

    if dry_run:
        click.echo("Is dry run")
        return

    click.echo(
        "Replace this message by putting your code into test_cli_project.cli.main"
    )
    click.echo("See click documentation at http://click.pocoo.org/")
