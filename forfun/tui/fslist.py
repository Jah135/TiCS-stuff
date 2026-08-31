from os import listdir
from os.path import isdir, basename

from pyansi import AnsiStyle, PaletteColor, Palette

from tui import Tree, render_tree
from charactersets import THIN_ROUNDED_MAPPING, THICK_MAPPING, THIN_MAPPING

file_style = AnsiStyle(fg=Palette(PaletteColor.BrightGreen))
dir_style = AnsiStyle(fg=Palette(PaletteColor.BrightBlue)).italic()


def create_tree_from_directory(
    dir_path: str, ignore_dirs: set[str] = set()
) -> Tree[str]:
    items = []

    for name in listdir(dir_path):
        full_path = dir_path + "/" + name

        if isdir(full_path) and not name in ignore_dirs:
            items.append(create_tree_from_directory(full_path, ignore_dirs))
        else:
            items.append(name)

    return Tree(basename(dir_path), items)


dir_tree = create_tree_from_directory("../../", {".git", "__pycache__"})
dir_tree.deep_sort()

print(render_tree(dir_tree, file_style, dir_style, cset=THIN_MAPPING))
