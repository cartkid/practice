import src.random_note as random_note

import unittest
import unittest.mock as mock


class Test(unittest.TestCase):
    list1 = random_note.Node(3)
    nodes1 = [4, 5, 6, 7, 8, 9, 10]
    random_note.create_nodes(list1, nodes1)

    list2 = random_note.Node(1)
    nodes2 = [2, 3, 4, 5, 6, 7, 8]
    random_note.create_nodes(list2, nodes2)

    @staticmethod
    def choice_five_node(values):
        for val in values:
            if val.val == 5:
                return val

    @staticmethod
    def choice_two_node(values):
        for val in values:
            if val.val == 2:
                return val

    def test_1(self):
        expected = 5
        result = None
        with mock.patch("random.choice", Test.choice_five_node):
            result = random_note.fetch_random_node(Test.list1)

        assert result.val == expected
        print("PASSED: Checking that we grab a random list node from `list1`")

    def test_2(self):
        expected = 2
        result = None
        with mock.patch("random.choice", Test.choice_two_node):
            result = random_note.fetch_random_node(Test.list2)

        assert result.val == expected
        print("PASSED: Checking that we grab a random list node from `list2`")

    def test_3(self):
        expected = 2
        result = None
        with mock.patch("random.choice", Test.choice_five_node):
            result = random_note.fetch_random_node(Test.list2)

        assert result.val != expected
        print("PASSED: Checking that we grab a random list node from `list2`")
