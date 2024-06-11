"""Module with main CLI function."""

import click


@click.group()
def cli() -> None:
    """Control interface for PHD badge."""
