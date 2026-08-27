from tui import render_tree, Tree
from os import listdir
from os.path import isdir, basename


def create_tree_from_directory(path: str) -> Tree:
    items = []

    for name in listdir(path):
        full_path = path + name

        if isdir(full_path):
            items.append(create_tree_from_directory(full_path))
        else:
            items.append(name)

    return Tree(basename(path), items)


print(
    render_tree(
        create_tree_from_directory("../../"),
    )
)
