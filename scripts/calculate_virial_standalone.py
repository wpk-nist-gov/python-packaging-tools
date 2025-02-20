# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pandas",
#     "tqdm>=4.67.1",
# ]
# ///
"""Script to calculate effective density"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from tqdm import tqdm

if TYPE_CHECKING:
    from collections.abc import Sequence


def _calculate_virial(sig: float, eps: float, lam: float, temp: float) -> float:
    out: float = (
        2 * np.pi / 3.0 * sig**3 * (1.0 + (1 - np.exp(-eps / temp)) * (lam**3 - 1.0))
    )
    return out


def _get_parser() -> argparse.ArgumentParser:
    """Get parser"""
    parser = argparse.ArgumentParser(
        prog="calclulate_virial",
        description="Script to calculate square-well-virial.",
    )

    parser.add_argument("filename", type=Path, help="input file")
    parser.add_argument(
        "output", type=Path, default=None, help="output file (optional)", nargs="?"
    )

    return parser


def main(args: Sequence[str] | None = None) -> int:
    """Main program."""
    parser = _get_parser()
    options = parser.parse_args() if args is None else parser.parse_args(args)
    data: pd.DataFrame = pd.read_csv(options.filename)  # pyright: ignore[reportUnknownMemberType]

    virial: list[float] = []
    for _, g in tqdm(data.iterrows(), total=len(data)):  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportUnknownVariableType]
        virial.append(
            _calculate_virial(sig=g.sig, eps=g.eps, lam=g.lam, temp=g.temp)  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
        )

    data_virial: pd.DataFrame = data.assign(virial=virial)  # pyright: ignore[reportUnknownMemberType]

    if options.output is None:
        print(data_virial)  # noqa: T201
    else:
        data_virial.to_csv(options.output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
