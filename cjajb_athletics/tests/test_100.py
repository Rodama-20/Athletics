
from src.cjajb_athletics.run.f100 import Flat100


def test_100_men_1199():
    assert Flat100.fsa_2010_men(9.98) == 1199


def test_100_men_1():
    assert Flat100.fsa_2010_men(21.10) == 1


def test_100_women_1199():
    assert Flat100.fsa_2010_women(10.86) == 1199


def test_100_women_1():
    assert Flat100.fsa_2010_women(21.42) == 1


def test_100_men_over_1200():
    assert Flat100.fsa_2010_men(9.00) == 1200


def test_100_women_over_1200():
    assert Flat100.fsa_2010_women(9.00) == 1200


def test_100_men_under_0():
    assert Flat100.fsa_2010_men(22.00) == 0


def test_100_women_under_0():
    assert Flat100.fsa_2010_women(22.00) == 0
