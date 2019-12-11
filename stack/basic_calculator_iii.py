class Solution:
    def calculate(self, s: str) -> int:
        s = s + "+0"
        return self.dfs(s, 0)

    def dfs(self, s, i):
        num, sign, stack = 0, '+', []

        while i < len(s):
            c = s[i]
            if c.isspace():
                i += 1
                continue
            elif c.isdigit():
                num = 10 * num + int(c)
                i += 1
            elif c == '(':
                num, i = self.dfs(s, i + 1)
            else:
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                elif sign == '*': stack.append(stack.pop() * num)
                elif sign == '/': stack.append(int(stack.pop() / num))

                num = 0
                i += 1
                if c == ')': return sum(stack), i
                sign = c

        return sum(stack)
