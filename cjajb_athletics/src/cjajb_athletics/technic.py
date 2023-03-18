"""
This module contains the technical discipline formula collection.
"""

import numpy as np


def _fsa_2010(
    performance: float | str | np.ndarray, _a: float, _b: float, _c: float
) -> int | np.ndarray:
    """Compute the points for a man using the FSA 2010 table."""
    if isinstance(performance, str):
        performance = float(performance)
    return np.floor(_a * ((100 * performance - _b) / 100) ** _c)
