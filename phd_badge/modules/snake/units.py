"""Game units."""

import random

from .constants import CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH


class Snake:
    """Snake."""

    def __init__(self) -> None:
        self.positions: list[tuple[int, int]] = [(100, 100)]
        self.direction: tuple[int, int] = (0, -1)

    def move(self) -> None:
        """Move snake."""
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)
        self.positions = [new_head] + self.positions[:-1]

    def grow(self) -> None:
        """Add snake length."""
        tail = self.positions[-1]
        self.positions.append(tail)

    def change_direction(self, new_direction: tuple[int, int]) -> None:
        """Change direction."""
        self.direction = new_direction

    def check_collision(self) -> bool:
        """Check snake collision with self and screen border."""
        head = self.positions[0]
        if head in self.positions[1:]:
            return True
        if not (0 <= head[0] < SCREEN_WIDTH and 0 <= head[1] < SCREEN_HEIGHT):
            return True
        return False


class Food:
    """Food."""

    def __init__(self) -> None:
        self.position: tuple[int, int] = self.random_position()

    def random_position(self) -> tuple[int, int]:
        """Generate random position."""
        x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)

    def respawn(self, exclude: list[tuple[int, int]]) -> None:
        """Move food to new random position."""
        while self.position in exclude:
            self.position = self.random_position()
