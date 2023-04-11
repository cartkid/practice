import src.fib as fib


def test_fib0():
    result = fib.fib(0)
    assert result == 0


def test_fib1():
    result = fib.fib(1)
    assert result == 1


def test_fib2():
    result = fib.fib(2)
    assert result == 1


def test_fib3():
    result = fib.fib(3)
    assert result == 2


def test_fib4():
    result = fib.fib(4)
    assert result == 3


def test_fib5():
    result = fib.fib(5)
    assert result == 5
