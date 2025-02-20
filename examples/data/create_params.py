"""Create params.csv file."""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

# * Logging
FORMAT = "[%(name)s - %(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


def main() -> None:
    """Get data and write"""
    out = [
        {
            "n": 2 * m,
            "m": m,
            "temp": temp,
            "dens": float(dens),
        }
        for m in range(2, 10)
        for temp in [0.5, 1.0, 1.5, 2.0, 3.0]
        for dens in [0.1, 0.2, 0.5, 0.8]
    ]

    path = Path(__file__).parent / "params.csv"
    pd.DataFrame(out).to_csv(path, index=False)
    logger.info("wrote %s", path)


if __name__ == "__main__":
    main()
