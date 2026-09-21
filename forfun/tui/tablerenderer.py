from typing import Any

from table import Table
from tui import render_table
from character_set import (
    SET_THIN_ROUNDED,
    SET_EMPTY,
    SET_THICK,
    SET_THIN_DASHED,
    SET_THIN,
    CharacterSet,
)

test_table: Table[Any] = Table(
    [[None] * 3 for _ in range(4)],
    row_headers=["hello", "goodbye", "hi", "use"],
    column_headers=["world", "column 2", "another column"],
)

test_table.write_column(0, (1, '"this is not an integer"', 9, 1e20))
test_table.write_row(1, (10, 20, "abcdefghijklmnkopqrstuvwxyz"))

print(test_table._data)
print(
    render_table(
        test_table,
        min_column_width=0,
        max_column_width=0,
        column_padding=2,
        cset=CharacterSet(v="|", cross="|", h=" ", fr="|", fl="|"),
    )
)
