class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, x: int) -> None:
        current_min = self.min_stack[-1] if self.min_stack else float('inf')
        self.stack.append(x)
        self.min_stack.append(min(current_min, x))

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()