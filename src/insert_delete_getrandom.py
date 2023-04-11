import random


class RandomizedSet:
    def __init__(self):
        self.items = set([])

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        self.items.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        self.items.discard(val)
        return True

    def getRandom(self) -> int:
        index_to_return: int = int(random.random() * len(self.items))
        return list(self.items)[index_to_return]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
