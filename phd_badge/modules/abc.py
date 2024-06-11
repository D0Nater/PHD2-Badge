"""Base class for modules."""

from time import sleep as time_sleep
from typing import Any

import requests

from phd_badge.schemas.pixel import Pixel


class BaseModule:
    """Base class for modules."""

    BADGE_URL = "http://badge.phd2/api/v1/led/picture"

    def __init__(self, delay: float):
        self._url = BaseModule.BADGE_URL
        self._delay = delay

    def run(self) -> None:
        """Run module."""
        raise NotImplementedError

    def send_to_badge(self, values: list[list[Pixel]]) -> None:
        """Send request to badge."""
        requests.post(
            self._url,
            json={"values": self._recursive_iter([[[pixel.r, pixel.g, pixel.b] for pixel in row] for row in values])},
        )

    def sleep(self, num: float | None = None) -> None:
        """Sleep."""
        time_sleep(num or self._delay)

    def _recursive_iter(self, arr: Any) -> Any:
        result = []
        for i in arr:
            if isinstance(i, list):
                result.extend(self._recursive_iter(i))
            else:
                result.append(i)
        return result
