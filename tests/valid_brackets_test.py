import src.valid_brackets as valid_brackets

import unittest


class Test(unittest.TestCase):
    def test_1(self):
        expected = True
        result = valid_brackets.Solution().isValid("()")

        assert result is expected

    def test_2(self):
        expected = True
        result = valid_brackets.Solution().isValid("()[]{}")

        assert result is expected

    def test_3(self):
        expected = False
        result = valid_brackets.Solution().isValid("()[{]}")

        assert result is expected

    def test_4(self):
        expected = False
        result = valid_brackets.Solution().isValid("(ab)[sx{sa]er}")

        assert result is expected

    def test_5(self):
        expected = True
        result = valid_brackets.Solution().isValid("(ab)[dx]{ew}a")

        assert result is expected

    def test_6(self):
        expected = True
        result = valid_brackets.Solution().isValid("(a[a{a}z]z)z")

        assert result is expected
