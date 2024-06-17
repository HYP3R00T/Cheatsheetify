from typing import Dict, Tuple, TypedDict


class Theme(TypedDict):
    colors: Dict[str, Tuple[int, int, int]]
    fonts: Dict[str, Tuple[str, str, str]]
    style: Dict[str, Tuple[str, str, int]]


Catppuccin: Theme = {
    "colors": {
        "background": (36, 39, 58),
        "title": (203, 166, 247),
        "credit": (184, 192, 224),
        "separator": (36, 39, 58),
        "command": (238, 153, 160),
        "command_fill": (24, 25, 38),
        "description": (245, 169, 127),
        "anchor": (138, 173, 244),
        "list_item": (166, 218, 149),
        "list_item_description": (202, 211, 245),
    },
    "fonts": [
        ("inter", "", "cheatsheetify/fonts/Inter.ttf"),
        ("inter", "I", "cheatsheetify/fonts/Inter-Italic.ttf"),
        ("firacode", "", "cheatsheetify/fonts/FiraCode.ttf"),
    ],
    "style": {
        "title": ("inter", "", 32),
        "credit": ("inter", "", 12),
        "command": ("inter", "", 16),
        "description": ("inter", "", 12),
        "anchor": ("firacode", "", 10),
        "list_item": ("firacode", "", 12),
        "list_item_description": ("inter", "I", 12),
    },
}
