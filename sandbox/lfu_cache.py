from heapq import heappush, heappop, heapify


class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __le__(self, other):
        return self.freq <= other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __ne__(self, other):
        return self.freq != other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __ge__(self, other):
        return self.freq >= other.freq


class LFUCache:
    def __init__(self, capacity: int):
        self.pq = []
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        node.freq += 1
        val = node.value
        heapify(self.pq)

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.freq += 1
            heapify(self.pq)
        else:
            node = Node(key, value, 1)
            self.cache[key] = node
            if len(self.pq) == self.capacity:
                del_node = heappop(self.pq)
                del self.cache[del_node.key]
            heappush(self.pq, node)

# Doesn't work if you need LRU for same frequency

# ["LFUCache", "put" "get"]
# [[0], [0, 0], [0]]
