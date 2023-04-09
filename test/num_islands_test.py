import src.num_islands as num_islands


def test_num_islands1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    actual = num_islands.num_islands(grid)
    assert actual == 1


def test_num_islands3():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    actual = num_islands.num_islands(grid)
    assert actual == 3


def test_num_islands0():
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    actual = num_islands.num_islands(grid)
    assert actual == 0


def test_num_islands10():
    grid = [
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
    ]
    actual = num_islands.num_islands(grid)
    assert actual == 10
