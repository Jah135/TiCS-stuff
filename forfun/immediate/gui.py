# TODO: do this https://github.com/dphfox/technical-fluff/blob/gh-pages/_drafts/i-made-my-perfect-ui-library.md

from pygame import Surface, Rect, draw
from pygame.typing import ColorLike
from pygame.font import Font

type Composition = list[Shape]


class Shape:
    min_x: int
    min_y: int

    max_x: int
    max_y: int

    def height(self) -> int:
        return self.max_y - self.min_y

    def width(self) -> int:
        return self.max_x - self.min_x

    def draw(self, surface: Surface): ...


class Quad(Shape):
    color: ColorLike
    roundness: int = -1

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: ColorLike,
        roundness: int = -1,
    ) -> None:
        self.min_x = x
        self.min_y = y
        self.max_x = x + width
        self.max_y = y + height
        self.color = color
        self.roundness = roundness

    def draw(self, surface: Surface):
        draw.rect(
            surface,
            self.color,
            Rect(self.min_x, self.min_y, self.width(), self.height()),
            border_radius=self.roundness,
        )


class Text(Shape):
    cached_text_surface: Surface

    def __init__(self, x: int, y: int, font: Font, text: str, color: ColorLike) -> None:
        rendered_text_surface = font.render(text, True, color)

        self.min_x = x
        self.min_y = y
        self.max_x = x + rendered_text_surface.width
        self.max_y = y + rendered_text_surface.height

        self.cached_text_surface = rendered_text_surface

    def draw(self, surface: Surface):
        # draw.rect(
        #     surface, "red", (self.min_x, self.min_y, self.width(), self.height()), 1
        # )
        surface.blit(self.cached_text_surface, (self.min_x, self.min_y))


def compose(*args: Shape | Composition) -> Composition:
    new_composition = []

    for shape_or_shapes in args:
        if isinstance(shape_or_shapes, list):
            new_composition.extend(shape_or_shapes)
        else:
            new_composition.append(shape_or_shapes)

    return new_composition


def draw_to_surface(composition: Composition, surface: Surface):
    for shape in composition:
        shape.draw(surface=surface)
