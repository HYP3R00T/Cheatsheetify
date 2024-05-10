<h1 align="center">Cheatsheetify</h1>

<p align="center">
<img alt="PyPI - Version" src="https://img.shields.io/pypi/v/cheatsheetify?style=for-the-badge&labelColor=%23363a4f&color=%23f5a97f&link=https%3A%2F%2Fpypi.org%2Fproject%2Fcheatsheetify%2F">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/HYP3R00T/Cheatsheetify/pypi_publish.yml?style=for-the-badge&labelColor=%23363a4f&color=%238aadf4">
</p>

cheatsheetify is a command-line tool that generates PDF versions of cheatsheets for popular command-line tools.

Documentation: [cheatsheetify.hyperoot.dev](https://cheatsheetify.hyperoot.dev/)

## Features

- Generates PDF cheatsheets for popular command-line tools.
- Easy to use with a simple command-line interface.
- Customizable output options.
- Custom themes for the PDFs

## Installation

To install cheatsheetify, you can use pip:

```sh
pip install cheatsheetify
```

## Usage

```sh
python cheatsheetify <list of commands>
```

For example, to generate a cheatsheet for `ls cp rm`, you would run:

```sh
python cheatsheetify ls cp rm
```

The generated PDF cheatsheet will be saved in the current directory. Read the [documentation](https://cheatsheetify.hyperoot.dev/) to learn more about the avialable customizations.

## Credits

This project would not have been possible without the awesome [tldr](https://tldr.sh/) project.

## Contributing

Contributions are welcome! If you'd like to add support for a new command-line tool or improve an existing cheatsheet, feel free to open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
