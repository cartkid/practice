import src.shifts as shifts


def test_compute_penalty_notopen_returns_0():
    result = shifts.compute_penalty("Y Y N Y", 0)
    expected = 3
    assert result == expected


def test_compute_penalty_opentwohours_returns_2():
    result = shifts.compute_penalty("N Y N Y", 2)
    expected = 2
    assert result == expected


def test_compute_penalty_openfourhours_returns_2():
    result = shifts.compute_penalty("Y Y N Y", 4)
    expected = 1
    assert result == expected


def test_compute_penalty_closedallhours_returns_4():
    result = shifts.compute_penalty("Y Y Y Y", 0)
    expected = 4
    assert result == expected


def test_compute_penalty_openallhours_returns_0():
    result = shifts.compute_penalty("Y Y Y Y", 4)
    expected = 0
    assert result == expected


def test_compute_penalty_closedallhours_returns_0():
    result = shifts.compute_penalty("N N N N", 0)
    expected = 0
    assert result == expected


def test_compute_penalty_openallhours_returns_4():
    result = shifts.compute_penalty("N N N N", 4)
    expected = 4
    assert result == expected


def test_find_best_closing_time1():
    result = shifts.find_best_closing_time("Y Y N N")
    expected = 2
    assert result == expected


def test_find_best_closing_time2():
    result = shifts.find_best_closing_time("Y Y Y N")
    expected = 3
    assert result == expected


def test_find_best_closing_time3():
    result = shifts.find_best_closing_time("N Y Y Y")
    expected = 4
    assert result == expected


def test_get_best_closing_times1():
    result = shifts.get_best_closing_times("BEGIN Y Y END \nBEGIN N N END")
    expected = [2, 0]
    assert result == expected


def test_get_best_closing_times2():
    result = shifts.get_best_closing_times(
        "BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END"
    )
    expected = [2]
    assert result == expected
