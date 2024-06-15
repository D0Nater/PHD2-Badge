"""Base class for modules."""

from time import sleep as time_sleep
from typing import Any

import requests
from requests import RequestException

from phd_badge.schemas.pixel import Pixel


class BaseModule:
    """Base class for modules."""

    BADGE_URL = "http://badge.phd2/api/v1/led/picture"

    def __init__(self, delay: float):
        self._delay = delay

    def run(self) -> None:
        """Run module."""
        raise NotImplementedError

    def send_to_badge(self, values: list[list[Pixel]]) -> None:
        """Send request to badge."""
        try:
            requests.post(
                BaseModule.BADGE_URL,
                json={
                    "values": self._recursive_iter([[[pixel.r, pixel.g, pixel.b] for pixel in row] for row in values])
                },
            )
        except RequestException as e:
            print(e)

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
