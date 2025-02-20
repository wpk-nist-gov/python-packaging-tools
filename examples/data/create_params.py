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
            "sig": 1.0,
            "eps": -1.0,
            "lam": lam,
            "temp": temp,
        }
        for lam in [0.1, 0.5, 1.0, 2.0]
        for temp in [0.5, 1.0, 2.0]
    ]

    path = Path(__file__).parent / "params.csv"
    pd.DataFrame(out).to_csv(path, index=False)
    logger.info("wrote %s", path)


if __name__ == "__main__":
    main()
