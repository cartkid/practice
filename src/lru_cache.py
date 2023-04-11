from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.items: dict[int, int] = {}
        self.capacity = capacity
        self.least_recently_used_cache: OrderedDict = OrderedDict()

    def get(self, key: int) -> int:
        return_me: int = self.least_recently_used_cache.get(key, -1)
        if return_me != -1:
            self.least_recently_used_cache.move_to_end(key)
        return return_me

    def put(self, key: int, value: int) -> None:
        existing_value: int = self.least_recently_used_cache.get(key, -1)
        self.least_recently_used_cache[key] = value
        if existing_value != -1:
            self.least_recently_used_cache.move_to_end(key)
        else:
            if len(self.least_recently_used_cache) > self.capacity:
                self.least_recently_used_cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
