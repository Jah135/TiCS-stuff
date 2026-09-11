from gui import Composition


class Rect:
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    @property
    def width(self) -> int:
        return self.max_x - self.min_x

    @property
    def height(self) -> int:
        return self.max_y - self.min_y

    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int) -> None:
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


def offset(shapes: Composition, x_offset: int, y_offset: int):
    for shape in shapes:
        shape.min_x += x_offset
        shape.max_x += x_offset
        shape.min_y += y_offset
        shape.max_y += y_offset


def get_bounds(shapes: Composition) -> Rect:
    return Rect(
        min(shapes, key=lambda shape: shape.min_x).min_x,
        min(shapes, key=lambda shape: shape.min_y).min_y,
        max(shapes, key=lambda shape: shape.max_x).max_x,
        max(shapes, key=lambda shape: shape.max_y).max_y,
    )
