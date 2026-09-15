class Tree[T]:
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
