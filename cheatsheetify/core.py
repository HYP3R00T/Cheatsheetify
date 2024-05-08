import subprocess
from typing import List, Dict


def generate_cheatsheet(command: str) -> Dict | str:
    try:
        output = subprocess.check_output(
            ["tldr", command], stderr=subprocess.STDOUT, universal_newlines=True
        )
        lines: List[str] = output.split("\n")
        infolines: List[str] = lines[:5]
        info_dict: Dict = {
            "command": command,
            "description": infolines[3].strip()[:-1],
            "homepage": infolines[-1].strip()[18:-1],
        }
        commandlines: List[str] = lines[6:]
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
        print(f"Error: {command} command not found or invalid.")
        return str(f"Error: {command} command not found or invalid.")


def main(commands: List[str]):
    for command in commands:
        print(generate_cheatsheet(command))
