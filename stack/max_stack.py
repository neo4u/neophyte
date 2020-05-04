class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        if not self.max_stack or x >= self.max_stack[-1][0]:
            self.max_stack.append((x, len(self.stack)))
        self.stack.append(x)

    def pop(self) -> int:
        result = self.stack.pop()
        if self.max_stack and self.max_stack[-1][0] == result:
            self.max_stack.pop()
        return result

    def top(self) -> int:
        if self.data:
            return self.stack[-1]

    def peekMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1][0]

    def popMax(self) -> int:
        if self.max_stack:
            md = self.max_stack.pop()
            self.stack.pop(md[1])
            for i in range(md[1], len(self.stack)):
                if not self.max_stack or self.data[i] >= self.max_stack[-1][0]:
                    self.max_stack.append((self.stack[i], i))
            return md[0]


# 716. Max Stack
# https://leetcode.com/problems/max-stack/description/


import heapq
class MaxStack:
    def __init__(self):
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
