class MaxStack:
    def __init__(self):
        self.max_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        current_max = self.max_stack[-1] if self.max_stack else float("-inf")
        self.stack.append(x)
        self.max_stack.append(max(current_max, x))

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        cur_max = self.max_stack[-1]

        tmp_stack = []
        while self.stack[-1] != cur_max:
            tmp_stack.append(self.pop())

        popped = self.pop()
        while tmp_stack:
            self.push(tmp_stack.pop())

        return popped

# 716. Max Stack
# https://leetcode.com/problems/max-stack/description/


import heapq
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.h = []
        self.l2d = set()
        self.h2d = set()
        self.id = 0

    def push(self, x: int) -> None:
        self.l.append((x, self.id))
        heapq.heappush(self.h, (-x, -self.id))
        self.id += 1

    def pop(self) -> int:
        self.top()
        x, i = self.l.pop()
        self.h2d.add(i)
        return x

    def top(self) -> int:
        while self.l[-1][1] in self.l2d:
            self.l2d.remove(self.l[-1][1])
            self.l.pop()
        return self.l[-1][0]

    def peekMax(self) -> int:
        while -self.h[0][1] in self.h2d:
            self.h2d.remove(-self.h[0][1])
            heapq.heappop(self.h)
        return -self.h[0][0]

    def popMax(self) -> int:
        self.peekMax()
        x, i = heapq.heappop(self.h)
        self.l2d.add(-i)
        return -x

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
