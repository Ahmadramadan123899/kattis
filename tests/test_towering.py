from src.kattis.towering import towering

def test_towering_case1():
    input_data = [12, 8, 2, 4, 10, 3, 25, 14]
    expected_output = [12, 10, 3, 8, 4, 2]
    result = towering(input_data)
    assert result == expected_output

def test_towering_case2():
    input_data = [1, 2, 3, 4, 5, 6, 6, 15]
    expected_output = [3, 2, 1, 6, 5,4] 
    result = towering(input_data)
    assert result == expected_output