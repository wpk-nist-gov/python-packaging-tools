"""
Core functionality (:mod:`~python_packaging_tools.core`)
========================================================
"""

from __future__ import annotations

import numpy as np


def calculate_virial(sig: float, eps: float, lam: float, temp: float) -> float:
    """
    Calculate second virial of square well fluid.

    Parameters
    ----------
    sig : float
        Size parameter.
    eps : float
        Depth of energy well (negative for attractive).
    lam : float
        Attrictive well size (lam * sig is well distance from sig)
    temp : float
        Reduced temperature.

    Returns
    -------
    float
        Second virial coefficient.

    Examples
    --------
    >>> calculate_virial(sig=1.0, eps=-1.0, lam=1.5, temp=1.0)
    -6.4526623819...
    """
    out: float = float(
        2 * np.pi / 3.0 * sig**3 * (1.0 + (1 - np.exp(-eps / temp)) * (lam**3 - 1.0))
    )
    return out
