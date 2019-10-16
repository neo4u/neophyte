# Approach 1: Using an Array and mod for wrap around
class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [0] * k
        self.head, self.tail = 0, -1
        self.capacity, self.size = k, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.tail = (self.tail + 1) % self.capacity
        self.arr[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.arr[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.arr[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Approach 2: Using a Cirularly Doubly Linked List
class Node:
    def __init__(self, value):
        self.val = value
        self.next, self.prev = None, None

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity, self.size = k, 0
        self.head = self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        node = Node(value)
        self._add(node)
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        node = self.head.next
        self._remove(node)
        self.size -= 1
        return True

    def _add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node.next.prev = node

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.next.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/description/


# Approach 1: Using an Array and mod for wrap around
# Approach 2: Using a Cirularly Doubly Linked List
