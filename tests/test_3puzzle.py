from src.kattis.puzzle import solve_puzzle


def test_already_solved():
    input_data = ["12", "3-"]
    assert solve_puzzle(input_data) == 0


def test_one_move():
    input_data = ["12", "-3"]
    assert solve_puzzle(input_data) == 1


def test_Unsolved_case():
    input_data = ["-1", "23"]
    assert solve_puzzle(input_data) == -1


def test_three_move():
    input_data = ["2-", "13"]
    assert solve_puzzle(input_data) == 3
