---
hide:
- navigation
---

<h1 align="center">Cheatsheetify</h1>

<p align="center">
<img alt="PyPI - Version" src="https://img.shields.io/pypi/v/cheatsheetify?style=for-the-badge&labelColor=%23363a4f&color=%23f5a97f&link=https%3A%2F%2Fpypi.org%2Fproject%2Fcheatsheetify%2F">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/HYP3R00T/Cheatsheetify/pypi_publish.yml?style=for-the-badge&labelColor=%23363a4f&color=%238aadf4">
</p>

cheatsheetify is a command-line tool that generates PDF versions of cheatsheets for popular command-line tools.

## Installation

<!-- termynal -->
```sh
pip install cheatsheetify
---> 100%
```

## Usage

### Basic

```sh
python cheatsheetify [commands]
```

For example, to generate a cheatsheet for `ls`, you would run:

```sh
python cheatsheetify ls
```

### Cheatsheet of multiple commands

We also have the option where you can pass a list of commands and we will generated a single PDF for all the cheatsheets of the commands.

```sh
python cheatsheetify ls cp rm
```

### Custom title

The title of the generated PDF can be changed using the `--title` flag.

```sh
python cheatsheetify ls --title "My cheatsheets"
```

### Custom PDF filename

The filename of the generated PDF can be changed using the `--filename` flag.

```sh
python cheatsheetify ls --filename "BestCheatsheet"
```

This example will generated the PDF as `BestCheatsheet.pdf`

### Custom theme

You can select the color scheme of the PDF from the available themes. You can use `--theme` flag to change the theme. The default theme is based on Catppuccin (Macchiato) theme.

```sh
python cheatsheetify ls --theme Nord
```

### Remove credit 😟

When the PDF is generated, right below the title, there is a link to this project. If you want to remove that, you can simply use `--no-credits` flag.

```sh
python cheatsheetify ls --no-credits
```

### CLI help

To show the help page, just use the `--help` flag.

```sh
python cheatsheetify --help
```

## Credits

This project would not have been possible without the awesome [tldr](https://tldr.sh/) project.

## Contributing

Contributions are welcome! If you'd like to add support for a new feature or themes, feel free to open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
