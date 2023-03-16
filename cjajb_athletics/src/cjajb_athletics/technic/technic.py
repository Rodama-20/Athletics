"""
This module contains the technical discipline formula collection.
"""

from math import floor

from ..discipline.discipline import Discipline


class Technic(Discipline):
    """Formula collection for run disciplines."""

    @staticmethod
    def fsa_2010_men(performance: float, a: float, b: float, c: float) -> int:
        """Compute the points for a man using the FSA 2010 table."""
        return floor(a * ((100 * performance - b) / 100) ** c)

    @staticmethod
    def fsa_2010_women(performance: float, a: float, b: float, c: float) -> int:
        """Compute the points for a woman using the FSA 2010 table."""
        return floor(a * ((100 * performance - b) / 100) ** c)
