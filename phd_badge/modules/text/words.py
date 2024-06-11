"""Words for text module."""

from abc import ABC, abstractmethod

from phd_badge.schemas.pixel import Pixel


class BaseWord(ABC):
    """Base word."""

    def __init__(self, pixel: Pixel | None = None, pixel_zero: Pixel | None = None) -> None:
        """Base word."""
        self._p0 = pixel_zero or Pixel(0, 0, 0)
        self._p1 = pixel or Pixel(255, 255, 255)

    @property
    @abstractmethod
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        raise NotImplementedError

    def _pixeles(self, values: list[str]) -> list[list[Pixel]]:
        return [[self._p0 if i == "0" else self._p1 for i in lst] for lst in values]


class WordZero(BaseWord):
    """Zero."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
            ]
        )


class WordHeart(BaseWord):
    """Heart."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011001100",
                "0111111110",
                "1111111111",
                "1111111111",
                "1111111111",
                "0111111110",
                "0011111100",
                "0000110000",
                "0000000000",
            ]
        )


class Word0(BaseWord):
    """0."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class Word1(BaseWord):
    """1."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0000110000",
                "0011110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0011111100",
                "0000000000",
            ]
        )


class Word2(BaseWord):
    """2."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0000000100",
                "0000001000",
                "0000010000",
                "0000100000",
                "0001000000",
                "0011111100",
                "0000000000",
            ]
        )


class Word3(BaseWord):
    """3."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0000000100",
                "0000011000",
                "0000000100",
                "0000000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class Word4(BaseWord):
    """4."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0011111100",
                "0000000100",
                "0000000100",
                "0000000100",
                "0000000100",
                "0000000000",
            ]
        )


class Word5(BaseWord):
    """5."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0010000000",
                "0010000000",
                "0011111000",
                "0000000100",
                "0000000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class Word6(BaseWord):
    """6."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000000",
                "0011111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class Word7(BaseWord):
    """7."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0000000100",
                "0000001000",
                "0000010000",
                "0000100000",
                "0001000000",
                "0010000000",
                "0000000000",
                "0000000000",
            ]
        )


class Word8(BaseWord):
    """8."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000100",
                "0001111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class Word9(BaseWord):
    """9."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000100",
                "0001111100",
                "0000000100",
                "0000000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordA(BaseWord):
    """A."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0011111100",
                "0010000100",
                "0010000100",
                "0000000000",
            ]
        )


class WordB(BaseWord):
    """B."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111000",
                "0010000100",
                "0010000100",
                "0011111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0011111000",
                "0000000000",
            ]
        )


class WordC(BaseWord):
    """C."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordD(BaseWord):
    """D."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011110000",
                "0010001000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010001000",
                "0011110000",
                "0000000000",
            ]
        )


class WordE(BaseWord):
    """E."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0010000000",
                "0010000000",
                "0010000000",
                "0011111000",
                "0010000000",
                "0010000000",
                "0011111100",
                "0000000000",
            ]
        )


class WordF(BaseWord):
    """F."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0010000000",
                "0010000000",
                "0011111000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0000000000",
            ]
        )


class WordG(BaseWord):
    """G."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000000",
                "0010000000",
                "0010011100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordH(BaseWord):
    """H."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0011111100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0000000000",
            ]
        )


class WordI(BaseWord):
    """I."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0011111100",
                "0000000000",
            ]
        )


class WordJ(BaseWord):
    """J."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0000011100",
                "0000000100",
                "0000000100",
                "0000000100",
                "0000000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordK(BaseWord):
    """K."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000000",
                "0010010000",
                "0010100000",
                "0011000000",
                "0011000000",
                "0010100000",
                "0010010000",
                "0010001000",
                "0000000000",
            ]
        )


class WordL(BaseWord):
    """L."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0011111100",
                "0000000000",
            ]
        )


class WordM(BaseWord):
    """M."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0011001100",
                "0010110100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0000000000",
            ]
        )


class WordN(BaseWord):
    """N."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0011000100",
                "0010100100",
                "0010100100",
                "0010010100",
                "0010010100",
                "0010001100",
                "0010000100",
                "0000000000",
            ]
        )


class WordO(BaseWord):
    """O."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordP(BaseWord):
    """P."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111000",
                "0010000100",
                "0010000100",
                "0011111000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0010000000",
                "0000000000",
            ]
        )


class WordQ(BaseWord):
    """Q."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000100",
            ]
        )


class WordR(BaseWord):
    """R."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011110000",
                "0010001000",
                "0010001000",
                "0011110000",
                "0011000000",
                "0010100000",
                "0010010000",
                "0010001000",
                "0000000000",
            ]
        )


class WordS(BaseWord):
    """S."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0001111000",
                "0010000100",
                "0010000000",
                "0001111000",
                "0000000100",
                "0000000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordT(BaseWord):
    """T."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000000000",
            ]
        )


class WordU(BaseWord):
    """U."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001111000",
                "0000000000",
            ]
        )


class WordV(BaseWord):
    """V."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0001001000",
                "0000110000",
                "0000000000",
            ]
        )


class WordW(BaseWord):
    """W."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010000100",
                "0010110100",
                "0011001100",
                "0010000100",
                "0000000000",
            ]
        )


class WordX(BaseWord):
    """X."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0001001000",
                "0000110000",
                "0000110000",
                "0001001000",
                "0010000100",
                "0010000100",
                "0000000000",
            ]
        )


class WordY(BaseWord):
    """Y."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0010000100",
                "0010000100",
                "0001001000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000110000",
                "0000000000",
            ]
        )


class WordZ(BaseWord):
    """Z."""

    @property
    def pixeles(self) -> list[list[Pixel]]:
        """Get word pixeles."""
        return self._pixeles(
            [
                "0000000000",
                "0011111100",
                "0000000100",
                "0000001000",
                "0000010000",
                "0000100000",
                "0001000000",
                "0010000000",
                "0011111100",
                "0000000000",
            ]
        )


WORDS: dict[str, type[BaseWord]] = {
    "0": Word0,
    "1": Word1,
    "2": Word2,
    "3": Word3,
    "4": Word4,
    "5": Word5,
    "6": Word6,
    "7": Word7,
    "8": Word8,
    "9": Word9,
    "a": WordA,
    "b": WordB,
    "c": WordC,
    "d": WordD,
    "e": WordE,
    "f": WordF,
    "g": WordG,
    "h": WordH,
    "i": WordI,
    "j": WordJ,
    "k": WordK,
    "l": WordL,
    "m": WordM,
    "n": WordN,
    "o": WordO,
    "p": WordP,
    "q": WordQ,
    "r": WordR,
    "s": WordS,
    "t": WordT,
    "u": WordU,
    "v": WordV,
    "w": WordW,
    "x": WordX,
    "y": WordY,
    "z": WordZ,
    " ": WordZero,
    "heart": WordHeart,
}
