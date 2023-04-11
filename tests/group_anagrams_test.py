import src.group_anagrams as group_anagrams


def test_group_anagrams1():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    result = group_anagrams.Solution().groupAnagrams(strs)
    print(result)

    assert compareListsOfLists(expected, result)


def compareListsOfLists(l1, l2):
    for item in l1:
        item.sort()
    for item in l2:
        item.sort()
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    return False
