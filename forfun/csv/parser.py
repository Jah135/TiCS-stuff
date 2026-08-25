from typing import Iterable, AbstractSet

class CSVTable:
    headers: list[str]
    rows: list[tuple[str, ...]]

    def __init__(self, headers: list[str]) -> None:
        self.headers = headers
        self.rows = []

    def add_row(self, row_data: AbstractSet[str]):
        if len(row_data) != len(self.headers):
            raise ValueError("invalid data row length")
        self.rows.append(tuple(row_data))

    def add_rows(self, rows: Iterable[AbstractSet[str]]):
        for row_data in rows:
            self.add_row(row_data)


    def __repr__(self) -> str:
        return f"CSVTable({self.headers})"

def parse_csv(source_lines: list[str]) -> CSVTable:
    headers = source_lines[0].split(",")

    return CSVTable(headers)

with open("dataset.csv", "r") as f:
    table = parse_csv(list(line[:-1] for line in f.readlines()))
    print(table)