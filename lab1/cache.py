from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        val = self.cache.pop(key, None)
        if val:
            self.cache[key] = val
            return val

        return ""

    def set(self, key: str, value: str) -> None:
        self.cache.pop(key, None)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            print(self.cache.popitem(last=False))

    def rem(self, key: str) -> None:
        self.cache.pop(key)
