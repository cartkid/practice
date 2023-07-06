import src.word_search as word_search


def test_word_search():
    grid1 = [
        ["b", "b", "b", "a", "l", "l", "o", "o"],
        ["b", "a", "c", "c", "e", "s", "c", "n"],
        ["a", "l", "t", "e", "w", "c", "e", "w"],
        ["a", "l", "o", "s", "s", "e", "c", "c"],
        ["w", "o", "o", "w", "a", "c", "a", "w"],
        ["i", "b", "w", "o", "w", "w", "o", "w"],
    ]
    word1_1 = "access"
    word1_2 = "balloon"
    word1_3 = "wow"
    word1_4 = "sec"
    word1_5 = "bbaal"

    grid2 = [
        ["a"],
    ]
    word2_1 = "a"

    grid3 = [
        ["c", "a"],
        ["t", "t"],
        ["h", "a"],
        ["a", "c"],
        ["t", "g"],
    ]
    word3_1 = "cat"
    word3_2 = "hat"

    grid4 = [
        ["c", "c", "x", "t", "i", "b"],
        ["c", "a", "t", "n", "i", "i"],
        ["a", "x", "n", "x", "p", "t"],
        ["t", "x", "i", "x", "t", "t"],
    ]
    word4_1 = "catnip"

    result = word_search.search(grid1, word1_1)
    assert result == [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]

    result = word_search.search(grid1, word1_2)
    assert result == [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]

    result = word_search.search(grid1, word1_5)
    assert result == [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]

    result = word_search.search(grid2, word2_1)
    assert result == [(0, 0)]

    result = word_search.search(grid3, word3_1)
    assert result == [(0, 0), (0, 1), (1, 1)]

    result = word_search.search(grid3, word3_2)
    assert result == [(2, 0), (3, 0), (4, 0)]
