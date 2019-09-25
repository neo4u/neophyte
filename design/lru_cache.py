class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prv, self.nxt = None, None


class LRUCache:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.hash_map = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        self._remove_node(node)
        self._add_to_front(node)

        return node.val

    def _remove_node(self, node):
        prv, nxt = node.prv, node.nxt
        if prv:
            prv.nxt = nxt
        if nxt:
            nxt.prv = prv

        if self.head == node:
            self.head = node.nxt
        if self.tail == node:
            self.tail = node.prv

    def _add_to_front(self, node):
        if self.head:
            self.head.prv = node
            node.nxt = self.head
            node.prv = None
            self.head = node
        else:
            self.head = node
            self.tail = node

    def put(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            self._remove_node(node)
            node.val = value
        else:
            node = Node(key, value)
            self.hash_map[key] = node

        self._add_to_front(node)

        if len(self.hash_map) > self.capacity:
            del self.hash_map[self.tail.key]
            self._remove_node(self.tail)
