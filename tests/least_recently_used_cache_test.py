import unittest
from src.least_recently_used_cache import Cache


class Test(unittest.TestCase):
    def test_1(self):
        cache = Cache(3)
        cache.put(1, 1)
        cache.put(2, 4)
        cache.put(3, 9)
        assert cache.get(1) == 1

        print("PASSED: Initialize a cache of size 3, and add/get items")

    def test_2(self):
        cache = Cache(3)
        cache.put(1, 1)
        cache.put(2, 4)
        cache.put(3, 9)
        cache.put(4, 16)
        assert cache.get(1) is None
        print("PASSED: `cache.put(4, 16);` should evict key `1`")

    def test_3(self):
        cache = Cache(2)
        cache.put(1, 1)
        cache.put(2, 4)
        cache.put(3, 9)
        assert cache.get(1) is None
        print("PASSED: `cache.put(4, 16);` should evict key `1`")

    def test_4(self):
        cache = Cache(2)
        cache.print()
        cache.print_reverse()
        cache.put(1, 1)
        cache.print()
        cache.print_reverse()
        cache.put(2, 2)
        cache.print()
        cache.print_reverse()
        cache.get(1)
        cache.print()
        cache.print_reverse()
        cache.put(3, 3)
        cache.print()
        cache.print_reverse()
        assert cache.get(2) is None
        print("PASSED: `cache.put(4, 16);` should evict key `1`")
