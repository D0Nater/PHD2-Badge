"""CLI commands for PHD badge.

All commands must be re-exported in this module, to launch code execution.
"""

from . import run
from .cli import cli


__all__ = ["cli", "run"]
