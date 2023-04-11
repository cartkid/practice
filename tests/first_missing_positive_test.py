import src.first_missing_positive as first_missing_positive


def test_first_missing_positive1():
    nums = [1, 2, 0]
    expected = 3
    result = first_missing_positive.Solution().firstMissingPositive(nums)
    assert expected == result


def test_first_missing_positive2():
    nums = [3, 4, -1, 1]
    expected = 2
    result = first_missing_positive.Solution().firstMissingPositive(nums)
    assert expected == result


def test_first_missing_positive3():
    nums = [7, 8, 9, 11, 12]
    expected = 1
    result = first_missing_positive.Solution().firstMissingPositive(nums)
    assert expected == result


def test_first_missing_positive4():
    nums = [1, 2, 4]
    expected = 3
    result = first_missing_positive.Solution().firstMissingPositive(nums)
    assert expected == result
