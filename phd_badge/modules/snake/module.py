"""Snake module."""

import pygame

from phd_badge.modules.abc import BaseModule
from phd_badge.schemas.pixel import Pixel

from .constants import CELL_SIZE, FOOD_COLOR, SCREEN_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_COLOR
from .units import Food, Snake


class SnakeModule(BaseModule):
    """Snake module."""

    def __init__(self, delay: float = 6):
        if delay <= 0:
            raise ValueError("Bad argument 'delay'")

        super().__init__(delay)

        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        self._snake = Snake()
        self._food = Food()
        self._running = True
        self._delay = delay

    def run(self) -> None:
        """Start game."""
        while self._running:
            self.handle_events()
            self.update()
            self.draw()
            self.send_to_badge(self.get_rgb_array())
            self._clock.tick(self._delay)
        pygame.quit()

    def handle_events(self) -> None:
        """Handle events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self._snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self._snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self._snake.change_direction((1, 0))

    def update(self) -> None:
        """Update game state."""
        self._snake.move()
        if self._snake.check_collision():
            self._running = False
        if self._snake.positions[0] == self._food.position:
            self._snake.grow()
            self._food.respawn(self._snake.positions)

    def draw(self) -> None:
        """Draw all elements."""
        self._screen.fill(SCREEN_COLOR)
        for pos in self._snake.positions:
            pygame.draw.rect(self._screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(
            self._screen, FOOD_COLOR, pygame.Rect(self._food.position[0], self._food.position[1], CELL_SIZE, CELL_SIZE)
        )
        pygame.display.flip()

    def get_rgb_array(self) -> list[list[Pixel]]:
        """Get RGB array from game map."""
        rgb_array: list[list[Pixel]] = []
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            row = []
            for x in range(0, SCREEN_WIDTH, CELL_SIZE):
                color = self._screen.get_at((x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                pixel = Pixel(r=color.r, g=color.g, b=color.b)
                row.append(pixel)
            rgb_array.append(row)
        return rgb_array
