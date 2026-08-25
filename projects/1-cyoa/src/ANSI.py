RESET = "\x1b[0m"

from enum import IntEnum

class PaletteColor(IntEnum):
    Black = 30
    Red = 31
    Green = 32
    Yellow = 33
    Blue = 34
    Magenta = 35
    Cyan = 36
    White = 37

    BrightBlack = 90
    BrightRed = 91
    BrightGreen = 92
    BrightYellow = 93
    BrightBlue = 94
    BrightMagenta = 95
    BrightCyan = 96
    BrightWhite = 97

    Default = 39

class AnsiColor:
    def get_sequence(self, background: bool) -> str: ...


class Palette(AnsiColor):
    def __init__(self, code: int) -> None:
        self.code = code

    def get_sequence(self, background: bool) -> str:
        code = self.code

        if background:
            code += 10

        return str(code)


class RGB8bit(AnsiColor):
    def __init__(self, index: int) -> None:
        self.index = index

    def get_sequence(self, background: bool) -> str:
        return f"{background and "48" or "38"};5;{self.index}"


class RGB24bit(AnsiColor):
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.color = (red, green, blue)

    def get_sequence(self, background: bool) -> str:
        (
            r,
            g,
            b,
        ) = self.color
        return f"{background and "48" or "38"};2;{r};{g};{b}"

def tint(text: str, color: AnsiColor, bg: bool = False):
    return f"\x1b[{color.get_sequence(bg)}m{text}{RESET}"