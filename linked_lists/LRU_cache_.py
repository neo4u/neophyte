class Node:
    def __init__(self, k=None, v=None):
        self.key, self.val = k, v
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            self._remove_first()

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev, node.next = p, self.tail
        self.tail.prev = node

    def _remove_first(self):
        first = self.head.next
        self._remove(first)
        self.cache.pop(first.key)

    def _remove(self, node):
        n, p = node.next, node.prev
        p.next, n.prev = n, p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)