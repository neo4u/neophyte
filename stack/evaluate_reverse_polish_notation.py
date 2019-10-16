from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, ops = [], frozenset(list('-+/*'))

        for token in tokens:
            if token in ops:
                r, l = int(stack.pop()), int(stack.pop())
                if token == '/':    v = int(l / r)
                elif token == '-':  v = l - r
                elif token == '+':  v = l + r
                elif token == '*':  v = l * r
                stack.append(v)
            else:
                stack.append(token)

        return stack.pop()


# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


sol = Solution()
assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
