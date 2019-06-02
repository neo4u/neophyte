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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

[
    "LRUCache",
    "put",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "get",
    "get",
    "put",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "get",
    "put",
    "get",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "get",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "get",
    "put",
    "get",
    "get",
    "get",
    "put",
    "get",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "get",
    "get",
    "get",
    "put",
    "put",
    "put",
    "put",
    "get",
    "put",
    "put",
    "put",
    "put",
    "put",
    "put",
    "put",
]
[
    [10],
    [10, 13],
    [3, 17],
    [6, 11],
    [10, 5],
    [9, 10],
    [13],
    [2, 19],
    [2],
    [3],
    [5, 25],
    [8],
    [9, 22],
    [5, 5],
    [1, 30],
    [11],
    [9, 12],
    [7],
    [5],
    [8],
    [9],
    [4, 30],
    [9, 3],
    [9],
    [10],
    [10],
    [6, 14],
    [3, 1],
    [3],
    [10, 11],
    [8],
    [2, 14],
    [1],
    [5],
    [4],
    [11, 4],
    [12, 24],
    [5, 18],
    [13],
    [7, 23],
    [8],
    [12],
    [3, 27],
    [2, 12],
    [5],
    [2, 9],
    [13, 4],
    [8, 18],
    [1, 7],
    [6],
    [9, 29],
    [8, 21],
    [5],
    [6, 30],
    [1, 12],
    [10],
    [4, 15],
    [7, 22],
    [11, 26],
    [8, 17],
    [9, 29],
    [5],
    [3, 4],
    [11, 30],
    [12],
    [4, 29],
    [3],
    [9],
    [6],
    [3, 4],
    [1],
    [10],
    [3, 29],
    [10, 28],
    [1, 20],
    [11, 13],
    [3],
    [3, 12],
    [3, 8],
    [10, 9],
    [3, 26],
    [8],
    [7],
    [5],
    [13, 17],
    [2, 27],
    [11, 15],
    [12],
    [9, 19],
    [2, 15],
    [3, 16],
    [1],
    [12, 17],
    [9, 1],
    [6, 19],
    [4],
    [5],
    [5],
    [8, 1],
    [11, 7],
    [5, 2],
    [9, 28],
    [1],
    [2, 2],
    [7, 4],
    [4, 22],
    [7, 24],
    [9, 26],
    [13, 28],
    [11, 26],
]

