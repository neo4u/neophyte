import collections

class Stack:
    def __init__(self):
        self.q = collections.deque([])

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()

    # @return an integer
    def top(self):
        return self.q[-1]

    # @return an boolean
    def empty(self):
        return len(self.q) == 0


# Python solution - O(1) (O(n) for push) 48ms

# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/