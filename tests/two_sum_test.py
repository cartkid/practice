import src.two_sum as two_sum


def test_two_sum1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    result = two_sum.Solution().twoSum(nums, target)
    assert result == expected


def test_two_sum2():
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    result = two_sum.Solution().twoSum(nums, target)
    assert result == expected


def test_two_sum3():
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    result = two_sum.Solution().twoSum(nums, target)
    assert result == expected


def test_two_sum4():
    nums = [2, 3]
    target = 6
    expected = []
    result = two_sum.Solution().twoSum(nums, target)
    assert result == expected
