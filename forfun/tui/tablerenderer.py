from typing import Any

from table import Table
from tui import render_table
from character_set import THIN_ROUNDED_MAPPING

test_table: Table[Any] = Table(
    ["hello", "goodbye", "hi", "use"], ["world", "column 2", "another column"]
)
test_table.write_column(0, (1, '"this is not an integer"', 9, 1e20))

print(render_table(test_table))
