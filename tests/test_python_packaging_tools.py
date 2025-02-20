"""Tests for `python-packaging-tools` package."""

from __future__ import annotations

from typing import Any

import numpy as np
import pytest

from python_packaging_tools import calculate_virial


def test_version() -> None:
    from python_packaging_tools import __version__

    assert __version__ != "999"


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        ((1.0, -1.0, 1.5, 1.0), -6.4526623819894455),
    ],
)
def test_calculate(args: tuple[Any, ...], expected: float) -> None:
    np.testing.assert_allclose(calculate_virial(*args), expected)
