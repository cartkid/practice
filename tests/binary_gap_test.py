import src.binary_gap as binary_gap


def test_binary_gap1():
    result = binary_gap.solution(1)
    assert result == 0


def test_binary_gap2():
    result = binary_gap.solution(1000000)
    assert result == 4
