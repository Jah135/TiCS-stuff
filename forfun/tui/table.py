from typing import Sequence


class Table[T]:
    row_headers: list[str]
    column_headers: list[str]

    _data: list[list[T]]

    @property
    def row_count(self) -> int:
        return len(self.row_headers)

    @property
    def column_count(self) -> int:
        return len(self.column_headers)

    def __init__(
        self, row_headers: list[str], column_headers: list[str], default: T = 0
    ) -> None:
        self.row_headers = row_headers
        self.column_headers = column_headers

        self._data = [[default] * self.column_count for _ in range(self.row_count)]

    def read_row(self, row_index: int) -> list:
        return self._data[row_index].copy()

    def write_row(self, row_index: int, values: Sequence[T]):
        row = self._data[row_index]

        for idx, item in enumerate(values):
            row[idx] = item

    def read_column(self, column_index: int) -> list:
        return [row[column_index] for row in self._data]

    def write_column(self, column_index: int, values: Sequence[T]):
        for idx, value in enumerate(values):
            self._data[idx][column_index] = values[idx]
