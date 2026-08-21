class CSVTable:
    headers: list[str]
    data: list[list[str]]

    def __init__(self, headers: list[str], data: list[list[str]]) -> None:
        self.headers = headers
        self.data = data

    def __repr__(self) -> str:
        return f"CSVTable({self.headers})"



def parse_csv(source_lines: list[str]) -> CSVTable:
    return CSVTable(source_lines[0].split(","), list(line.split(",") for line in source_lines[1:]))

with open("dataset.csv", "r") as f:
    table = parse_csv(list(line[:-1] for line in f.readlines()))
    print(table)