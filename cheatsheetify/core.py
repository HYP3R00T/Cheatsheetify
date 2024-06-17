import os
from enum import Enum
from typing import List

import typer
from typing_extensions import Annotated

from cheatsheetify.pdf_generator import generate_pdf


class Schema(str, Enum):
    Catppuccin = "Catppuccin"
    Nord = "Nord"
    Rose = "Rose"


def is_valid_path(path: str) -> bool:
    return os.path.exists(path[0]) and len(path) == 1


def main(
    commands: Annotated[
        List[str],
        typer.Argument(
            help="List of commands to generate cheatsheet.pdf", show_default=False
        ),
    ],
    title: Annotated[str, typer.Option(help="Provide the title")] = "Cheat Sheet",
    filename: Annotated[
        str, typer.Option(help="Provide the filename for PDF")
    ] = "cheatsheet",
    theme: Annotated[Schema, typer.Option(help="Select a theme")] = Schema.Catppuccin,
    credits: Annotated[
        bool, typer.Option(help="Give credit to cheatsheetify in PDF")
    ] = True,
):
    input_values = {
        "commands": commands,
        "title": title,
        "filename": filename,
        "theme": theme,
        "credits": credits,
    }

    if is_valid_path(commands):
        # TODO: Add feature to allow path
        pass
    else:
        generate_pdf(input_values)
