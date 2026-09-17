from typing import Any

from table import Table
from tui import render_table
from character_set import THIN_ROUNDED_MAPPING

test_table: Table[Any] = Table(
    [[None] * 3 for _ in range(4)],
    row_headers=["hello", "goodbye", "hi", "use"],
    column_headers=["world", "column 2", "another column"],
)

test_table.write_column(0, (1, '"this is not an integer"', 9, 1e20))
test_table.write_row(1, (10, 20, "lee"))

print(test_table._data)
print(render_table(test_table, max_column_width=90, column_padding=20))
