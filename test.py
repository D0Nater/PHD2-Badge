"""Game units."""

import random
import sys
from typing import List, Tuple

import pygame


# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CELL_SIZE = 20
SCREEN_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
FPS = 10


class Snake:
    """Класс, представляющий собой Змейку в игре."""

    def __init__(self) -> None:
        self.positions: List[Tuple[int, int]] = [(100, 100)]
        self.direction: Tuple[int, int] = (0, -1)

    def move(self) -> None:
        """Двигает змейку в текущем направлении."""
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)
        self.positions = [new_head] + self.positions[:-1]

    def grow(self) -> None:
        """Увеличивает длину змейки на одну клетку."""
        tail = self.positions[-1]
        self.positions.append(tail)

    def change_direction(self, new_direction: Tuple[int, int]) -> None:
        """Меняет направление движения змейки."""
        self.direction = new_direction

    def check_collision(self) -> bool:
        """Проверяет столкновение змейки с самой собой или с границами экрана."""
        head = self.positions[0]
        if head in self.positions[1:]:
            return True
        if not (0 <= head[0] < SCREEN_WIDTH and 0 <= head[1] < SCREEN_HEIGHT):
            return True
        return False


class Food:
    """Класс, представляющий собой Еду в игре."""

    def __init__(self) -> None:
        self.position: Tuple[int, int] = self.random_position()

    def random_position(self) -> Tuple[int, int]:
        """Генерирует случайную позицию для еды."""
        x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)

    def respawn(self) -> None:
        """Перемещает еду в новую случайную позицию."""
        self.position = self.random_position()


class Game:
    """Класс, представляющий собой игру "Змейка"."""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True

    def handle_events(self) -> None:
        """Обрабатывает события (например, нажатия клавиш)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))

    def update(self) -> None:
        """Обновляет состояние игры (позиции змейки и еды)."""
        self.snake.move()
        if self.snake.check_collision():
            self.running = False
        if self.snake.positions[0] == self.food.position:
            self.snake.grow()
            self.food.respawn()

    def draw(self) -> None:
        """Рисует все элементы на экране."""
        self.screen.fill(SCREEN_COLOR)
        for pos in self.snake.positions:
            pygame.draw.rect(self.screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(
            self.screen, FOOD_COLOR, pygame.Rect(self.food.position[0], self.food.position[1], CELL_SIZE, CELL_SIZE)
        )
        pygame.display.flip()

    def run(self) -> None:
        """Запускает главный цикл игры."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
