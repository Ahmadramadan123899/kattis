from src.kattis.abcproblem import reorder_nb

def test_standard_order():
    assert reorder_nb("1 2 3", "ABC") == "1 2 3"

def test_reversed_order():
    assert reorder_nb("1 2 3", "CBA") == "3 2 1"

def test_mixed_order():
    assert reorder_nb("1 2 3", "ACB") == "1 3 2"

def test_unsorted_input():
    assert reorder_nb("3 1 2", "BAC") == "2 1 3"