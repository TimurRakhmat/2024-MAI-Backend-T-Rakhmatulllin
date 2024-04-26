class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = dict()

    def get(self, key: str) -> str:
        val = self.cache.pop(key, None)
        if val:
            self.cache[key]=val
            return val
        else:
            return ""

    def set(self, key: str, value: str) -> None:
        self.cache.pop(key, None)
        self.cache[key]=value

        #if len(self.cache) > self.capacity:
            #print(self.cache.popitem()

    def rem(self, key: str) -> None:
        self.cache.pop(key)