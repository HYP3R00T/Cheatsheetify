import subprocess
from typing import List, Dict
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from typing_extensions import Annotated
import typer
import json
import re

from cheatsheetify.pdf_generator import generate_pdf


def generate_cheatsheet(command: str) -> Dict | str:
    try:
        output = subprocess.check_output(
            ["tldr", command], stderr=subprocess.STDOUT, universal_newlines=True
        )
        lines: List[str] = output.split("\n")
        infolines: List[str] = []
        commandlines: List[str] = []
        blank_line = 0
        for idx, line in enumerate(lines):
            if blank_line == 3:
                infolines = lines[:idx]
                commandlines = lines[idx:]
                break
            elif line == "":
                blank_line += 1
        info_dict: Dict = {
            "command": command,
            "description": " ".join(x.strip() for x in infolines[3:-2]),
            "homepage": re.search(r"https?://\S+", infolines[-2].strip()).group()[:-1],
        }
        comamnd_dict: Dict = {}
        temp: str = ""
        for line in commandlines:
            if line.strip().startswith("-"):
                temp = line.strip()[2:-1]
            elif line.strip().startswith(command):
                if line.strip() not in comamnd_dict.keys():
                    comamnd_dict[line.strip()] = temp
        cheatsheet_dict: Dict = {"info": info_dict, "commands": comamnd_dict}
        return json.dumps(cheatsheet_dict)
    except subprocess.CalledProcessError:
        print(f"Error: {command} command not found or invalid.")
        return str(f"Error: {command} command not found or invalid.")


def main(
    commands: Annotated[
        List[str], typer.Argument(help="List of commands to generate cheatsheet.pdf")
    ]
):
    doc = SimpleDocTemplate("cheatsheet.pdf", pagesize=A4)
    elements: List = []
    for command in commands:
        generate_pdf(generate_cheatsheet(command), elements)
    doc.build(elements)