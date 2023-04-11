import src.balance_string as balance_string


def test_balance_string():
    result = balance_string.balance_string("aaab")
    assert result == 2


def test_balance_string2():
    result = balance_string.balance_string("aaabbb")
    assert result == 0


def test_balance_string3():
    result = balance_string.balance_string("")
    assert result == 0
