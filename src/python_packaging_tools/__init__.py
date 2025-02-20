"""
Top level API (:mod:`python_packaging_tools`)
======================================================
"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _version

from .core import calculate_virial

try:
    __version__ = _version("python-packaging-tools")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "999"


__author__ = """William P. Krekelberg"""
__email__ = "wpk@nist.gov"


__all__ = [
    "__version__",
    "calculate_virial",
]
