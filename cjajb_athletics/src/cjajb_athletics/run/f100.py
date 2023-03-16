"""
Return the points for a 100m run.
"""

from .run import Run


class Flat100(Run):
    """
    Return the points for a 100m run.
    """

    @staticmethod
    def fsa_2010_men(performance: float, _a=7.080303, _b=2150, _c=2.1) -> int:
        """Compute the points for a man using the FSA 2010 table."""

        return Run.fsa_2010_men(performance, _a, _b, _c)

    @staticmethod
    def fsa_2010_women(performance: float, _a=7.89305, _b=2180, _c=2.1) -> int:
        """Compute the points for a woman using the FSA 2010 table."""

        return Run.fsa_2010_women(performance, _a, _b, _c)
