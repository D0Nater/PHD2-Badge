"""Matrix module."""

import numpy as np

from phd_badge.modules.abc import BaseModule
from phd_badge.schemas.pixel import Pixel


class MatrixModule(BaseModule):
    """Matrix module."""

    def __init__(self, delay: float = 0.1, frequency: float = 0.15):
        if delay <= 0:
            raise ValueError("Bad argument 'delay'")
        if 0 > frequency > 1:
            raise ValueError("Bad argument 'frequency'. Must be (0 <= frequency <= 1)")

        super().__init__(delay)

        self._rows = 10
        self._cols = 10
        self._matrix = np.array([[Pixel(0, 0, 0) for _ in range(self._cols)] for _ in range(self._rows)])
        self._frequency = frequency

    def run(self) -> None:
        """Run module."""
        while True:
            self.update_matrix()
            self.send_to_badge(self._recursive_iter(self._matrix))
            self.sleep()

    def update_matrix(self) -> None:
        """Updates the matrix by shifting pixels down, adding new drops and leaving a trace."""
        # Moving all pixels down
        for i in range(self._rows - 1, 0, -1):
            for j in range(self._cols):
                self._matrix[i][j] = self._matrix[i - 1][j]
        # Adding new drops from above
        for j in range(self._cols):
            if np.random.rand() < self._frequency:  # The probability of a new drop
                self._matrix[0][j] = Pixel(0, 255, 0)  # Green pixel
            else:
                self._matrix[0][j] = Pixel(0, 0, 0)  # Black Pixel
        # Leaving a trail
        for i in range(1, self._rows):
            for j in range(self._cols):
                if self._matrix[i][j].g == 255 and i > 0:
                    # Reducing the green channel
                    self._matrix[i - 1][j].g = max(0, self._matrix[i][j].g - 150)
                    if i > 1:
                        self._matrix[i - 2][j].g = max(0, self._matrix[i][j].g - 220)
