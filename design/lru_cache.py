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




class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None) # dummy node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def remove(self, node=None):
        if self._size == 0: return
        if not node: node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node
