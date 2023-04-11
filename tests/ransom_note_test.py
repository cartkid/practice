import src.ransom_note as ransom_note


def test_ransom_note1():
    ransomNote = "a"
    magazine = "b"
    expected = False
    result = ransom_note.Solution().canConstruct(ransomNote, magazine)
    assert expected == result


def test_ransom_note2():
    ransomNote = "aa"
    magazine = "ab"
    expected = False
    result = ransom_note.Solution().canConstruct(ransomNote, magazine)
    assert expected == result
