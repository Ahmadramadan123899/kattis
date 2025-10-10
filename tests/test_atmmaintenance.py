from src.kattis.atmmaintenance import atmmaintenance

def test_all_withdrawals_successful():
    assert atmmaintenance("4 10", "2 2 2 2") == [1, 1, 1, 1]

def test_partial_success():
    assert atmmaintenance("4 5", "2 2 2 2") == [1, 1, 0, 0]

def test_none_successful():
    assert atmmaintenance("3 1", "2 3 4") == [0, 0, 0]

def test_exact_balance():
    assert atmmaintenance("3 6", "2 2 2") == [1, 1, 1]

def test_zero_balance():
    assert atmmaintenance("2 0", "1 2") == [0, 0]