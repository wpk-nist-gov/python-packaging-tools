"""
Core functionality (:mod:`~python_packaging_tools.core`)
========================================================
"""

from __future__ import annotations

from typing import cast

import analphipy


def calculate_effective_density(
    n: int,
    m: int,
    temp: float,
    dens: float,
    sig: float = 1.0,
    eps: float = 1.0,
) -> float:
    """
    Calculate effective density using Noro-Frenkel analysis of Mie potential

    Parameters
    ----------
    n, m : int
        Mie potential parameters.
    temp : float
        Temperature.
    dens : float
        Density.
    sig, eps : float
        Mie potential parameters.

    Returns
    -------
    float
        Effective density.

    Examples
    --------
    >>> calculate_effective_density(12, 6, 1.0, 0.5)
    0.52377532...
    """
    p = analphipy.potential.LennardJonesNM(n=n, m=m, sig=sig, eps=eps)
    nf = p.to_nf()

    sig = cast("float", nf.sig(beta=1 / temp))

    return dens * sig**3
