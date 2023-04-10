import src.is_happy as is_happy


def test_is_happy1():
    result = is_happy.isHappy(1)
    assert result is True


def test_is_happy2():
    result = is_happy.isHappy(2)
    assert result is False


def test_is_happy3():
    result = is_happy.isHappy(19)
    assert result is True
