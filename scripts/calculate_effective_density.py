# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "analphipy",
#     "pandas",
#     "tqdm>=4.67.1",
# ]
# ///
"""Script to calculate effective density"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import TYPE_CHECKING, cast

import analphipy
import pandas as pd
from tqdm import tqdm

if TYPE_CHECKING:
    from collections.abc import Sequence


def _calculate_effective_density(n: int, m: int, temp: float, dens: float) -> float:
    p = analphipy.potential.LennardJonesNM(n=n, m=m)
    nf = p.to_nf()

    sig = cast("float", nf.sig(beta=1 / temp))

    return dens * sig**3


def _get_parser() -> argparse.ArgumentParser:
    """Get parser"""
    parser = argparse.ArgumentParser(
        prog="calculate_effective_density",
        description="Script to calculate effective density.",
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

    dens_eff: list[float] = []
    for _, g in tqdm(data.iterrows(), total=len(data)):  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportUnknownVariableType]
        dens_eff.append(
            _calculate_effective_density(n=g.n, m=g.m, temp=g.temp, dens=g.dens)  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
        )

    data_eff: pd.DataFrame = data.assign(dens_eff=dens_eff)  # pyright: ignore[reportUnknownMemberType]

    if options.output is None:
        print(data_eff)  # noqa: T201
    else:
        data_eff.to_csv(options.output)

    return 0


if __name__ == "__main__":
    sys.exit(main())
