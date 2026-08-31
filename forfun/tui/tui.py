from pyansi import AnsiStyle

from charactersets import CharacterSet, THIN_MAPPING


def render_inside_box(
    contents_text: str,
    width: int = 10,
    height: int = 4,
    mapping: CharacterSet = THIN_MAPPING,
) -> str:
    contents_lines = contents_text.splitlines()
    lines = []

    lines.append(mapping.tl + mapping.h * (width - 2) + mapping.tr)

    for index in range(height - 2):
        content = ""

        if index < len(contents_lines):
            content = contents_lines[index]

        lines.append(
            mapping.v + (content + " " * (width - len(content) - 2)) + mapping.v
        )

    lines.append(mapping.bl + mapping.h * (width - 2) + mapping.br)

    return "\n".join(lines)


class Tree[T: AnsiStyle]:
    name: str
    items: list[T | Tree]

    def __repr__(self) -> str:
        return f"Tree({self.name}, {self.items})"

    def __init__(self, name: str, items: list[T | Tree]) -> None:
        self.name = name
        self.items = items

    def shallow_sort(self):
        self.items.sort(key=lambda x: str(x))
        self.items.sort(key=lambda x: isinstance(x, Tree), reverse=False)

    def deep_sort(self):
        self.shallow_sort()

        for value in self.items:
            if isinstance(value, Tree):
                value.deep_sort()


def render_tree(
    tree: Tree,
    item_style: AnsiStyle = AnsiStyle(),
    dir_style: AnsiStyle = AnsiStyle(),
    cset: CharacterSet = THIN_MAPPING,
) -> str:
    lines = []

    for index, value in enumerate(tree.items):
        is_last = index == len(tree.items) - 1

        if isinstance(value, Tree):
            nested = render_tree(value, item_style, dir_style, cset)

            lines.append(
                (cset.bl if is_last else cset.fr)
                + cset.h
                + " "
                + dir_style.apply_with_reset(value.name + "/")
            )

            for line in nested.splitlines():
                lines.append((" " if is_last else cset.v) + "  " + line)
        else:
            lines.append(
                (cset.bl if is_last else cset.fr)
                + cset.h
                + " "
                + item_style.apply_with_reset(str(value))
            )

    return "\n".join(lines)
