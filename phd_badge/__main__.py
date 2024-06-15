"""Main entry point."""

from os import environ


environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from .cli import cli  # noqa: E402


def main() -> None:
    """Call the CLI."""
    cli()


if __name__ == "__main__":
    main()
