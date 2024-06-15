"""Run commands."""

from typing import get_args as get_type_args

import click

from phd_badge.modules import SnakeModule, TextModule
from phd_badge.modules.text.module import ModeType

from .cli import cli


@cli.group()
def run() -> None:
    """Run commands."""


@run.command("text")
@click.option("--text", "-t", default=":zov:", help='Text. Examples: ("phd2", ":zov:", ":svo:", ":mom:").')
@click.option("--mode", "-m", default="sliderLeft", help=f"Mode {get_type_args(ModeType)}.")
@click.option("--delay", "-d", default=0.15, help="Delay animation.")
@click.option("--repeats", "-r", default=-1, help="Repeats.")
def text_module(text: str, mode: ModeType, delay: float, repeats: int) -> None:
    """Text module."""
    module = TextModule(text, mode, delay, repeats)
    module.run()


@run.command("snake")
@click.option("--delay", "-d", default=6, help="Delay animation.")
def snake_module(delay: float) -> None:
    """Text module."""
    module = SnakeModule(delay)
    module.run()
