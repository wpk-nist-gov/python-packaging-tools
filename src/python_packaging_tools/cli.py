"""
Console script (:mod:`~python_packaging_tools.cli`)
==========================================================
"""

import sys

import typer

PACKAGE = "python_packaging_tools"

app = typer.Typer()


@app.command()
def func() -> int:
    """Console script for python_packaging_tools."""
    print(f"Replace this message by putting your code into {PACKAGE}.cli.main")  # noqa: T201
    print("See click documentation at https://typer.tiangolo.com/")  # noqa: T201
    return 0


# get the click function. For use with sphinx-click
main = typer.main.get_command(app)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
