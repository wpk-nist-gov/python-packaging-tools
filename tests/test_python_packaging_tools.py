"""Tests for `python-packaging-tools` package."""

from __future__ import annotations

import pytest
from click.testing import CliRunner

from python_packaging_tools import cli, example_function


def test_version() -> None:
    from python_packaging_tools import __version__

    assert __version__ != "999"


@pytest.fixture
def response() -> tuple[int, int]:
    return 1, 2


def test_example_function(response: tuple[int, int]) -> None:
    expected = 3
    assert example_function(*response) == expected


def test_command_line_interface() -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "python_packaging_tools.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help" in help_result.output
    assert "Show this message and exit." in help_result.output
