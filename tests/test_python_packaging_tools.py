"""Tests for `python-packaging-tools` package."""

from __future__ import annotations

from typing import Any

import numpy as np
import pytest

from python_packaging_tools import calculate_effective_density


def test_version() -> None:
    from python_packaging_tools import __version__

    assert __version__ != "999"


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        ((12, 6, 1.0, 0.5), 0.5237753242357204),
    ],
)
def test_calculate(args: tuple[Any, ...], expected: float) -> None:
    np.testing.assert_allclose(calculate_effective_density(*args), expected)
