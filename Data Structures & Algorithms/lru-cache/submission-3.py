class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        response = self.cache.pop(key,-1)
        if response != -1:
            self.cache[key] = response

        return response

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            least_used = next(iter(self.cache))
            del self.cache[least_used]

        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value

