from src.kattis.different import different


def test_basic_differences():
    input_data = ["10 4", "3 8", "100 100"]
    assert different(input_data) == [6, 5, 0]


def test_negative_values():
    input_data = ["-5 5", "0 -10"]
    assert different(input_data) == [10, 10]


def test_large_numbers():
    input_data = ["1000000000 1", "999999999 0"]
    assert different(input_data) == [999999999, 999999999]
