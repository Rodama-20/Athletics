"""
This module contains the technical discipline formula collection.
"""

from ._formula import Performance, Score, fsa_2010


def _fsa_2010(performance: Performance, _a: float, _b: float, _c: float) -> Score:
    """Compute points using the FSA 2010 table."""
    return fsa_2010(performance, _a, _b, _c, lower_is_better=False)


# Men tables
def high_jump_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the high jump men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 732.15375, 75, 1)


def pole_vault_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the pole vault men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 234.78771, 80, 1)


def long_jump_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the long jump men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 136.08157, 130, 1.1)


def triple_jump_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the triple jump men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 86.950221, 395, 1)


def shot_put_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the shot put men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 82.491673, 178, 0.9)


def discus_throw_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the discus throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 28.891406, 494, 0.9)


def hammer_throw_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the hammer throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 24.978132, 581, 0.9)


def javelin_throw_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the javelin throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 23.247477, 602, 0.9)


def ball_throw_men(performance: Performance) -> Score:
    """Give the points obtained for a performance in the ball throw men venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 19.191528, 600, 0.9)


# Women tables
def high_jump_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the high jump women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 942.65514, 75, 1)


def pole_vault_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the pole vault women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 303.79747, 80, 1)


def long_jump_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the long jump women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 171.91361, 125, 1.1)


def triple_jump_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the triple jump women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 106.044538, 374, 1)


def shot_put_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the shot put women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 83.435373, 130, 0.9)


def discus_throw_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the discus throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 27.928062, 362, 0.9)


def hammer_throw_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the hammer throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 25.267696, 405, 0.9)


def javelin_throw_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the javelin throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 28.058125, 360, 0.9)


def ball_throw_women(performance: Performance) -> Score:
    """Give the points obtained for a performance in the ball throw women venue.

    Args:
        performance (float | str | np.ndarray): The distance in m for an athlete or an array of performances.

    Returns:
        int | np.ndarray: The points for the performance or an array of points.
    """
    return _fsa_2010(performance, 24.63917, 500, 0.9)
