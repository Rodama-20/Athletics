"""
The module computes the points for a run discipline.

Cyrille Polier 2023
"""

import numpy as np


def _fsa_2010(
    performance: float | str | np.ndarray, _a: float, _b: float, _c: float
) -> int | np.ndarray:
    """Compute the points using the FSA 2010 table.

    Parameters for the formula can be found on the Swiss Athletics website:
    https://swiss-athletics.ch/fr/baremes/
    https://swiss-athletics.ch/de/wertungstabellen/

    Args:
        performance (float | str | np.ndarray): The performance in seconds for an athlete or an array of performances.
        _a (float): The a parameter for the formula given in the FSA 2010 table.
        _b (float): The b parameter for the formula given in the FSA 2010 table.
        _c (float): The c parameter for the formula given in the FSA 2010 table.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """

    if isinstance(performance, np.ndarray):
        points = _a * np.power((100 * performance - _b) / 100, _c, dtype=complex)
        points = np.where(np.isreal(points), 0, points)
        points = np.abs(points)
        return np.minimum(np.floor(points), 1200)

    if isinstance(performance, str):
        performance = float(performance)

    point = _a * ((_b - 100 * performance) / 100) ** _c
    point = 0 if isinstance(point, complex) else point
    return np.minimum(np.floor(point), 1200)


def flat_100_men(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 100m flat for a men race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 7.080303, 2150, 2.1)


def flat_100_women(performance: float | str | np.ndarray) -> int | np.ndarray:
    """Give the points obtained for a performance in the 100m flat for a women race.

    Args:
        performance (float | str | np.ndarray): The time in seconds for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 7.89305, 2180, 2.1)
