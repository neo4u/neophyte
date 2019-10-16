class Node:
    def __init__(self, k, v):
        self.prev, self.next = None, None
        self.key, self.val = k, v


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hash_map: return -1

        node = self.hash_map[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self._remove(node)
            node.val = value
        else:
            node = Node(key, value)
            self.hash_map[key] = node
        self._add(node)

        if len(self.hash_map) > self.capacity:
            self.hash_map.pop(self.tail.prev.key)
            self._remove(self.tail.prev)

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.prev.next = node.next.prev = node

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p


# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/
