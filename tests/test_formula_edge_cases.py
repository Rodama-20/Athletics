"""Edge cases shared by running and technical disciplines."""

import numpy as np

import cjajb_athletics.run as Run
import cjajb_athletics.technic as Technic


def test_scalar_returns_python_int():
    assert type(Run.flat_100_men(10.0)) is int
    assert type(Run.flat_100_men(np.float64(10.0))) is int
    assert type(Technic.long_jump_men(np.float64(8.0))) is int


def test_array_returns_integer_array():
    scores = Run.flat_100_men(np.array([10.0, 22.0]))
    assert isinstance(scores, np.ndarray)
    assert np.issubdtype(scores.dtype, np.integer)
    assert np.array_equal(scores, np.array([1195, 0]))


def test_array_like_sequences_are_supported():
    assert np.array_equal(Run.flat_100_men([10.0, 22.0]), np.array([1195, 0]))
    assert np.array_equal(Technic.long_jump_men((8.0, 0.0)), np.array([1102, 0]))


def test_invalid_numeric_values_score_zero():
    values = np.array([np.nan, np.inf, -np.inf, -1.0])
    assert np.array_equal(Run.flat_100_men(values), np.zeros(4, dtype=int))
    assert np.array_equal(Technic.long_jump_men(values), np.zeros(4, dtype=int))


def test_empty_array_is_supported():
    scores = Run.flat_100_men(np.array([]))
    assert isinstance(scores, np.ndarray)
    assert scores.size == 0
