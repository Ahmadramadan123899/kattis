from src.kattis.ataleoftwoqueues import atableoftwoqueues

def test_left_faster():
    input_data = ["2 2","1 2","3 4"]
    assert atableoftwoqueues(input_data) == "left"

def test_right_faster():
    input_data = [
        "3 2",
        "5 5 5",
        "1 1"
    ]
    assert atableoftwoqueues(input_data) == "right"

def test_equal_times():
    input_data = [
        "2 2",
        "2 3",
        "1 4"
    ]
    assert atableoftwoqueues(input_data) == "either"