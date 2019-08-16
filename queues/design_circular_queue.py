class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.arr = [0]*k
        self.size = 0
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int):
        if self.isFull(): return False

        self.tail = (self.tail + 1) % self.capacity
        self.arr[self.tail] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty(): return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.arr[self.head]

    def Rear(self):
        return -1 if self.isEmpty() else self.arr[self.tail]

    def isEmpty(self):
        return True if self.size == 0 else False

    def isFull(self):
        return True if self.size == self.capacity else False



# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/description/

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
