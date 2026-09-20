"""Shared scoring formulas used by the public athletics modules."""

from collections.abc import Sequence
from typing import TypeAlias

import numpy as np

Performance: TypeAlias = float | int | str | np.number | Sequence[float] | np.ndarray
Score: TypeAlias = int | np.ndarray


def fsa_2010(
    performance: Performance,
    a: float,
    b: float,
    c: float,
    *,
    lower_is_better: bool,
) -> Score:
    """Compute points using the Swiss Athletics FSA 2010 formula.

    Scalar input produces a Python ``int``. Array-like input produces a NumPy
    integer array with the same shape. Invalid numeric performances (negative,
    NaN or infinite) and performances outside the scoring domain produce zero
    points. Scores are capped to the official 0..1200 range.
    """
    values = np.asarray(performance, dtype=float)
    scalar_input = values.ndim == 0

    if lower_is_better:
        base = (b - 100.0 * values) / 100.0
    else:
        base = (100.0 * values - b) / 100.0

    valid = np.isfinite(values) & (values >= 0.0) & (base > 0.0)
    powered = np.zeros_like(values, dtype=float)
    np.power(base, c, out=powered, where=valid)

    points = np.floor(a * powered)
    points = np.clip(points, 0, 1200).astype(np.int64, copy=False)

    if scalar_input:
        return int(points.item())
    return points
