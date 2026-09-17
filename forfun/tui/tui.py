from typing import Any

from pyansi import AnsiStyle

from character_set import CharacterSet, THIN_MAPPING
from tree import Tree
from table import Table


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


def _get_char_length(x: Any) -> int:
    return len(str(x))


def _get_column_width(table: Table, column_index: int) -> int:
    return max(
        _get_char_length(x)
        for x in (
            table.column_headers[column_index],
            *table.read_column(column_index),
        )
    )


def _format_cell_content(x: Any, fit_width: int) -> str:
    x_str = str(x)
    x_str_len = len(x_str)

    if x_str_len > fit_width:
        if fit_width > 3:
            return (x_str[: fit_width - 3] + "...").rjust(fit_width)
        else:
            return x_str[:fit_width].rjust(fit_width)

    return x_str.rjust(fit_width)


def render_table(
    table: Table,
    cset: CharacterSet = THIN_MAPPING,
    max_column_width: int = 100,
    column_padding: int = 1,
) -> str:
    lines = []

    row_header_width: int = (
        min(
            max_column_width,
            max(_get_char_length(header) for header in table.row_headers),
        )
        + column_padding * 2
    )
    column_widths: tuple[int, ...] = tuple(
        min(max_column_width, _get_column_width(table, idx)) + (column_padding * 2)
        for idx in range(table.column_count)
    )

    lines.append(
        cset.tl
        + cset.fd.join(cset.h * width for width in (row_header_width, *column_widths))
        + cset.tr
    )
    lines.append(
        cset.v
        + " " * row_header_width
        + cset.v
        + cset.v.join(
            _format_cell_content(header, column_widths[col_index])
            for (col_index, header) in enumerate(table.column_headers)
        )
        + cset.v
    )
    lines.append(
        cset.fr
        + cset.cross.join(
            cset.h * width for width in (row_header_width, *column_widths)
        )
        + cset.fl
    )

    for row_header, row_data in zip(table.row_headers, table._data):
        lines.append(
            cset.v
            + _format_cell_content(row_header, row_header_width)
            + cset.v
            + cset.v.join(
                _format_cell_content(x, column_widths[col_index])
                for (col_index, x) in enumerate(row_data)
            )
            + cset.v
        )

    lines.append(
        cset.bl
        + cset.fu.join(cset.h * width for width in (row_header_width, *column_widths))
        + cset.br
    )

    return "\n".join(lines)
