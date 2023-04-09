import src.hailstone as hailstone


def test_hailstone0():
    result = hailstone.hailstone(0)
    assert result == 0


def test_hailstone1():
    result = hailstone.hailstone(1)
    assert result == 0


def test_hailstone2():
    result = hailstone.hailstone(2)
    assert result == 1


def test_hailstone27():
    result = hailstone.hailstone(27)
    assert result == 111


def test_hailstone4():
    result = hailstone.hailstone(4)
    assert result == 2


def test_hailstone3():
    result = hailstone.hailstone(3)
    assert result == 7
