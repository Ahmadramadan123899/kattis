from src.kattis.areal import areal

def test_area_5():
    assert areal("5") == round(4*(5**0.5),6)

def test_area_1():
    assert areal("1") ==4.0

def test_area_100():
    assert areal("100") ==40.0