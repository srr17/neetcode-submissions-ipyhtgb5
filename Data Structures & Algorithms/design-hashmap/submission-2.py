class MyHashMap:

    def __init__(self):
        self.size = 10**6 + 1
        self.map = [-1] * self.size

    def put(self, key: int, value: int) -> None:
        if 0 <= key < self.size:
            self.map[key] = value

    def get(self, key: int) -> int:
        if 0 <= key < self.size:
            return self.map[key]
        return -1

    def remove(self, key: int) -> None:
        if 0 <= key < self.size:
            self.map[key] = -1