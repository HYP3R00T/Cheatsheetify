from typing import List, Dict
import subprocess
import re


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
        return cheatsheet_dict
    except subprocess.CalledProcessError:
        return command
