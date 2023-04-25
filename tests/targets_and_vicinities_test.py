import src.targets_and_vicinities as targets_and_vicinities
import unittest


def test_targets_and_vicinities_1():
    actual = "45624"
    guess = "24325"
    expect = "1T2V"
    result = targets_and_vicinities.getTV(actual, guess)
    assert result == expect


class Test(unittest.TestCase):
    def test_1(self):
        assert targets_and_vicinities.getTV("345", "135") == "1T1V"
        print("PASSED: getTV('345', '135') should return '1T1V'")

    def test_2(self):
        assert targets_and_vicinities.getTV("01", "01") == "2T0V"
        print("PASSED: getTV('01', '01') should return '2T0V'")

    def test_3(self):
        assert targets_and_vicinities.getTV("130", "893") == "0T1V"
        print("PASSED: getTV('130', '893') should return '0T1V'")
