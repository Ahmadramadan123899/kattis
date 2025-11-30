from src.kattis.aaah import can_john_go


def test_exact_match():
    assert can_john_go("aaaah", "aaaah") == "go"


def test_more_as():
    assert can_john_go("aaaaaah", "aaaah") == "go"


def test_not_enough_as():
    assert can_john_go("aah", "aaaah") == "no"


def test_non_a_characters():
    assert can_john_go("ahmad", "aaa") == "no"
