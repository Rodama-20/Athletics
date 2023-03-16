"""
This module contains the running discipline formula collection.
"""

from math import floor

from ..discipline.discipline import Discipline


class Run(Discipline):
    """Formula collection for run disciplines."""

    @staticmethod
    def fsa_2010_men(performance: float, _a: float, _b: float, _c: float) -> int:
        """Compute the points for a man using the FSA 2010 table."""
        try:
            return min(floor(_a * ((_b - 100 * performance) / 100) ** _c), 1200)
        except TypeError:
            return 0

    @staticmethod
    def fsa_2010_women(performance: float, _a: float, _b: float, _c: float) -> int:
        """Compute the points for a woman using the FSA 2010 table."""
        try:
            return min(floor(_a * ((_b - 100 * performance) / 100) ** _c), 1200)
        except TypeError:
            return 0
