"""
This module contains the running discipline formula collection.
"""

import numpy as np


def _fsa_2010(
    performance: float | str | np.ndarray, _a: float, _b: float, _c: float
) -> int | np.ndarray:
    """Compute the points for a man using the FSA 2010 table."""

    if isinstance(performance, np.ndarray):
        points = _a * np.power((100 * performance - _b) / 100,  _c, dtype=complex)
        points = np.where(np.isreal(points), 0, points)
        points = np.abs(points)
        return np.minimum(np.floor(points), 1200)
    
    if isinstance(performance, str):
        performance = float(performance)

    point = _a * ((_b - 100 * performance) / 100) ** _c    
    point = 0 if isinstance(point, complex) else point
    return np.minimum(np.floor(point), 1200)


def flat_100_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Compute the points for a man using the FSA 2010 table."""
    return _fsa_2010(performance, 7.080303, 2150, 2.1)


def flat_100_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Compute the points for a woman using the FSA 2010 table."""
    return _fsa_2010(performance, 7.89305, 2180, 2.1)
