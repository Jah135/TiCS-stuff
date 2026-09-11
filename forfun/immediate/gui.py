# TODO: do this https://github.com/dphfox/technical-fluff/blob/gh-pages/_drafts/i-made-my-perfect-ui-library.md


class Shape:
    min_x: int
    min_y: int

    max_x: int
    max_y: int

    def height(self) -> int:
        return self.max_y - self.min_y

    def width(self) -> int:
        return self.max_x - self.min_x

    def draw(self): ...


def offset(shapes: list[Shape], x_offset: int, y_offset: int):
    for shape in shapes:
        shape.min_x += x_offset
        shape.max_x += x_offset
        shape.min_y += y_offset
        shape.max_y += y_offset
