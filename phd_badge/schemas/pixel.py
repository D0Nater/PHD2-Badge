"""Pixel shemas."""

from dataclasses import dataclass


@dataclass
class Pixel:
    """Pixel."""

    r: int
    g: int
    b: int

    @property
    def to_list(self) -> list[int]:
        """Return list [R, G, B]."""
        return [self.r, self.g, self.b]
