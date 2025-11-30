from src.kattis.floors13 import floors


def test_below_13():
    assert floors(12) == 12


def test_exact_13():
    assert floors(13) == 14


def test_above_13():
    assert floors(14) == 15
    assert floors(20) == 21


def test_edge_case_1():
    assert floors(1) == 1
