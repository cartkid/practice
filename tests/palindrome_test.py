import src.palindrome as palindrome


def test_palindrome_1():
    val = "racecar"
    expected = True
    result = palindrome.is_palindrome(val)
    assert result is expected


def test_palindrome_2():
    val = "a"
    expected = True
    result = palindrome.is_palindrome(val)
    assert result is expected


def test_palindrome_3():
    val = "ab"
    expected = False
    result = palindrome.is_palindrome(val)
    assert result is expected
