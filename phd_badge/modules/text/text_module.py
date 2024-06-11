"""Text module."""

from typing import Literal, get_args as get_type_args

import numpy as np

from phd_badge.modules.abc import BaseModule
from phd_badge.modules.text.words import WORDS, BaseWord
from phd_badge.schemas.pixel import Pixel


ModeType = Literal["switching", "sliderUp", "sliderLeft"]


class TextModule(BaseModule):
    """Text module."""

    def __init__(self, text: str = ":zov:", mode: ModeType = "sliderLeft", delay: float = 0.1, repeats: int = -1):
        if delay <= 0:
            raise ValueError("Bad argument 'delay'")
        elif repeats < -1:
            raise ValueError("Bad argument 'repeats'")

        super().__init__(delay)

        self._text = text.lower()
        self._mode = mode.lower()
        self._repeats = repeats
        self._mode_func = {
            "switching": self.switching_text,
            "sliderup": self.slider_text_up,
            "sliderleft": self.slider_text_left,
        }
        self._text_func = {
            ":svo:": [
                WORDS["s"](Pixel(255, 255, 255)),
                WORDS["v"](Pixel(0, 75, 234)),
                WORDS["o"](Pixel(255, 0, 0)),
            ],
            ":zov:": [
                WORDS["z"](Pixel(255, 255, 255)),
                WORDS["o"](Pixel(0, 75, 234)),
                WORDS["v"](Pixel(255, 0, 0)),
            ],
            ":mom:": [
                WORDS["i"](),
                WORDS["heart"](Pixel(255, 0, 0)),
                WORDS["u"](),
                WORDS["r"](),
                WORDS["m"](),
                WORDS["o"](),
                WORDS["m"](),
            ],
        }

        if self._mode not in self._mode_func:
            raise ValueError(f"Mode {mode} not found.\nAvailable: {get_type_args(ModeType)}")

    def run(self) -> None:
        """Run module."""
        i = 0
        while self._repeats == -1 or i < self._repeats:
            self._mode_func[self._mode](self._text_func.get(self._text) or self._get_text_words())
            i += 1

    def switching_text(self, words: list[BaseWord]) -> None:
        """Switching text."""
        for word in words:
            self.send_to_badge(word.pixeles)
            self.sleep()

    def slider_text_left(self, words: list[BaseWord]) -> None:
        """Slider text left."""
        words.insert(0, WORDS[" "]())
        words.append(WORDS[" "]())

        arr = np.zeros((10, len(words) * 10), dtype=Pixel)

        for word_num, word in enumerate(words):
            for word_row_idx, word_row in enumerate(word.pixeles):
                for pixel_idx, pixel in enumerate(word_row):
                    arr[word_row_idx][pixel_idx + (word_num * 10)] = pixel

        for i in range(arr.shape[1] - 9):
            arr = np.roll(arr, -1, axis=1)
            self.send_to_badge(self._recursive_iter(arr[:, :10]))
            self.sleep()

    def slider_text_up(self, words: list[BaseWord]) -> None:
        """Slider text up."""
        words.insert(0, WORDS[" "]())
        words.append(WORDS[" "]())

        arr = np.zeros((len(words) * 10, 10), dtype=Pixel)

        for word_num, word in enumerate(words):
            for word_row_idx, word_row in enumerate(word.pixeles):
                for pixel_idx, pixel in enumerate(word_row):
                    arr[word_row_idx + (word_num * 10)][pixel_idx] = pixel

        for i in range(arr.shape[0] - 9):
            arr = np.roll(arr, -1, axis=0)
            self.send_to_badge(self._recursive_iter(arr[:10, :]))
            self.sleep()

    def _get_text_words(self) -> list[BaseWord]:
        words: list[BaseWord] = []

        for i in self._text.split(":"):
            if i in WORDS:
                words.append(WORDS[i]())
            else:
                for j in i:
                    words.append(WORDS[j]())

        return words
