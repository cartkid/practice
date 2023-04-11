import src.insert_delete_getrandom as insert_delete_getrandom


def test_insert_delete_getrandom0():
    obj = insert_delete_getrandom.RandomizedSet()
    param_1 = obj.insert(1)
    assert param_1 is True
    param_2 = obj.remove(2)
    assert param_2 is False
    param_3 = obj.insert(2)
    assert param_3 is True
    param_4 = obj.getRandom()
    assert param_4 == 2 or param_4 == 1
    param_5 = obj.remove(1)
    assert param_5 is True
    param_6 = obj.insert(2)
    assert param_6 is False
    param_7 = obj.getRandom()
    assert param_7 == 2 or param_7 == 1
