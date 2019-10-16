# Approach 1: Using an Array and mod for wrap around
class MyCircularDeque:
    def __init__(self, k):
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._data = [-1] * k

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value):
        if self.isFull(): return False

        if self.isEmpty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self):
        if self.isEmpty(): return False

        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self):
        if self.isEmpty(): return False

        self._data[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1

        if self.isEmpty(): self._front = self._rear
        return True

    def getFront(self):
        return self._data[self._front]

    def getRear(self):
        return self._data[self._rear]

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == self._capacity

# Approach 2: Using a Cirularly Doubly Linked List
class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None


class MyCircularDeque:
    def __init__(self, k):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k
        self.curSize = 0

    def add(self, value, preNode):
        new = Node(value)
        new.pre = preNode
        new.next = preNode.next
        new.pre.next = new.next.pre = new
        self.curSize += 1

    def remove(self, preNode):
        node = preNode.next
        node.pre.next = node.next
        node.next.pre = node.pre
        self.curSize -= 1

    def insertFront(self, value):
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value):
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self):
        if self.curSize:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self):
        if self.curSize:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        if self.curSize: return self.head.next.val
        return -1

    def getRear(self):
        if self.curSize:
            return self.tail.pre.val
        return -1

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size


# 641. Design Circular Deque
# https://leetcode.com/problems/design-circular-deque/description/


# Approach 1: Using an Array and mod for wrap around
# Approach 2: Using a Cirularly Doubly Linked List
