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


def test_palindrome2_1():
    val = "racecar"
    expected = True
    result = palindrome.is_palindrome2(val)
    assert result is expected


def test_palindrome2_2():
    val = "12344321"
    expected = True
    result = palindrome.is_palindrome2(val)
    assert result is expected


def test_palindrome2_3():
    val = "1234321"
    expected = True
    result = palindrome.is_palindrome2(val)
    assert result is expected


def test_palindrome2_4():
    val = "1234567"
    expected = False
    result = palindrome.is_palindrome2(val)
    assert result is expected


def test_palindrome3_1():
    val = "racecar"
    expected = True
    result = palindrome.is_palindrome3(val)
    assert result is expected


def test_palindrome3_2():
    val = "12344321"
    expected = True
    result = palindrome.is_palindrome3(val)
    assert result is expected


def test_palindrome3_3():
    val = "1234321"
    expected = True
    result = palindrome.is_palindrome3(val)
    assert result is expected


def test_palindrome3_4():
    val = "1234567"
    expected = False
    result = palindrome.is_palindrome3(val)
    assert result is expected
