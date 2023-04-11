import src.sanitize_sort as sanitize_sort


def test_sanitize_sort1():
    result = sanitize_sort.sanitize("a, b,   c, 1, 3, 4, 5, 6, 2, 4, 4, 4")
    assert [1, 2, 3, 4, 5, 6] == result
