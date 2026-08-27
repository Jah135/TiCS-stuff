from typing import AbstractSet


class CharacterMapping:
    h: str
    v: str
    tl: str
    tr: str
    bl: str
    br: str
    fr: str
    fl: str
    fd: str
    fu: str

    def __init__(
        self,
        h: str,
        v: str,
        tl: str,
        tr: str,
        bl: str,
        br: str,
        fr: str,
        fl: str,
        fd: str,
        fu: str,
    ) -> None:
        self.h = h
        self.v = v
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br
        self.fr = fr
        self.fl = fl
        self.fd = fd
        self.fu = fu


THIN_H = "\u2500"
THIN_V = "\u2502"
THIN_TL = "\u250c"
THIN_TR = "\u2510"
THIN_BL = "\u2514"
THIN_BR = "\u2518"
THIN_H_DASHED = "\u254c"
THIN_V_DASHED = "\u254e"
THIN_TL_ROUNDED = "\u256d"
THIN_TR_ROUNDED = "\u256e"
THIN_BR_ROUNDED = "\u256f"
THIN_BL_ROUNDED = "\u2570"
THIN_FR = "\u251c"
THIN_FL = "\u2524"
THIN_FD = "\u252c"
THIN_FU = "\u2534"

THICK_H = "\u2501"
THICK_V = "\u2503"
THICK_TL = "\u250f"
THICK_TR = "\u2513"
THICK_BL = "\u2517"
THICK_BR = "\u251b"

THIN_MAPPING = CharacterMapping(
    h=THIN_H,
    v=THIN_V,
    tl=THIN_TL,
    tr=THIN_TR,
    bl=THIN_BL,
    br=THIN_BR,
    fr=THIN_FR,
    fl=THIN_FL,
    fd=THIN_FD,
    fu=THIN_FU,
)
# THIN_DASHED_MAPPING = CharacterMapping(
#     THIN_H_DASHED,
#     THIN_V_DASHED,
#     THIN_TL,
#     THIN_TR,
#     THIN_BL,
#     THIN_BR,
# )
# THIN_ROUNDED_MAPPING = CharacterMapping(
#     THIN_H,
#     THIN_V,
#     THIN_TL_ROUNDED,
#     THIN_TR_ROUNDED,
#     THIN_BL_ROUNDED,
#     THIN_BR_ROUNDED,
# )
# THICK_MAPPING = CharacterMapping(
#     THICK_H,
#     THICK_V,
#     THICK_TL,
#     THICK_TR,
#     THICK_BL,
#     THICK_BR,
# )


def render_inside_box(
    contents_text: str,
    width: int = 10,
    height: int = 4,
    mapping: CharacterMapping = THIN_MAPPING,
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


class Tree:
    name: str
    items: list[str | Tree]

    def __repr__(self) -> str:
        return f"Tree({self.name}, {self.items})"

    def __init__(self, name: str, items: list[str | Tree]) -> None:
        self.name = name
        self.items = items


def render_tree(tree: Tree, mapping: CharacterMapping = THIN_MAPPING) -> str:
    lines = []

    for index, value in enumerate(tree.items):
        is_last = index == len(tree.items) - 1

        if type(value) == str:
            lines.append(
                (mapping.bl if is_last else mapping.fr) + mapping.h * 2 + " " + value
            )
        elif type(value) == Tree:
            nested = render_tree(value, mapping)

            lines.append(
                (mapping.bl if is_last else mapping.fr) + mapping.h + " " + value.name
            )

            for line in nested.splitlines():
                lines.append((" " if is_last else mapping.v) + "  " + line)

    return "\n".join(lines)
