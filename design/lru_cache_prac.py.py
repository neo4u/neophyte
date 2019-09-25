class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prv, self.nxt = None, None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_node = {}
        self.head, self.tail = None, None

    def get(self, key):
        if key not in self.key_to_node: return -1

        node = self.key_to_node[key]
        self._remove_node(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove_node(node)
            node.value = value
        else:
            node = Node(key, value)
            self.key_to_node[key] = node

        self._add_to_front(node)

        if len(self.key_to_node) > self.capacity:
            self.key_to_node.pop(self.tail.key)
            self._remove_node(self.tail)

    def _remove_node(self, node):
        prv, nxt = node.prv, node.nxt                       # Find the prev and next node to the node to remove
        if prv: prv.nxt = nxt                               # Make the prev node's nxt pointer point to the node after the node to add
        if nxt: nxt.prv = prv                               # Make the next node's prv pointer point to the node before the node to remove

        if self.head == node: self.head = self.head.nxt     # Update head to node after it, if the node to remove was at head
        if self.tail == node: self.tail = self.tail.prv     # Update tail to node before it, if the node to remove was at tail

    def _add_to_front(self, node):

        if self.head:
            node.nxt, node.prv = self.head, None
            self.head = node
