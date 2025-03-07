"""
Console script (:mod:`~python_packaging_tools.cli`)
==========================================================
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd
from tqdm import tqdm

from .core import calculate_virial

if TYPE_CHECKING:
    from collections.abc import Sequence


def get_parser() -> argparse.ArgumentParser:
    """Get parser"""
    parser = argparse.ArgumentParser(
        prog="sw-second-virial",
        description="Script to calculate second virial coefficient of square well fluid.",
    )

    parser.add_argument("filename", type=Path, help="input file")
    parser.add_argument(
        "output", type=Path, default=None, help="output file (optional)", nargs="?"
    )

    return parser


def main(args: Sequence[str] | None = None) -> int:
    """Main program."""
    parser = get_parser()
    options = parser.parse_args() if args is None else parser.parse_args(args)
    data: pd.DataFrame = pd.read_csv(options.filename)  # pyright: ignore[reportUnknownMemberType]

    dens_eff: list[float] = []
    for _, g in tqdm(data.iterrows(), total=len(data)):  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportUnknownVariableType]
        dens_eff.append(
            calculate_virial(sig=g.sig, eps=g.eps, lam=g.lam, temp=g.temp)  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
        )

    data_eff: pd.DataFrame = data.assign(dens_eff=dens_eff)  # pyright: ignore[reportUnknownMemberType]

    if options.output is None:
        print(data_eff)  # noqa: T201
    else:
        data_eff.to_csv(options.output)

    return 0
