import src.lru_cache as lru_cache


def test_lru_cache1():
    obj = lru_cache.LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    get1 = obj.get(1)
    assert get1 == 1
    obj.put(3, 3)
    get2 = obj.get(2)
    assert get2 == -1
    obj.put(4, 4)
    get3 = obj.get(1)
    assert get3 == -1
    get4 = obj.get(3)
    assert get4 == 3
    get5 = obj.get(4)
    assert get5 == 4
