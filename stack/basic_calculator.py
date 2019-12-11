import re

# Approach 1: Regex and Stack
class Solution1:
    def arithmetic(self, res, op, num):
        if not op:  res = num
        else:       res += num * [-1, 1][(op == "+") * 1]
        return res

    def calculate(self, s):
        res, op, stack = 0, None, []

        for ch in re.findall(r"(\d+|[+-]|\(|\))", s):
            if ch.isdigit():
                res = self.arithmetic(res, op, int(ch))
            elif ch in ["+", "-"]:
                op = ch
            elif ch == "(":
                stack.extend([op, res])
                res, op = 0, None
            elif ch == ")":
                res = self.arithmetic(stack.pop(), stack.pop(), res)

        return res


# Approach 2: 1 Stack
class Solution:
    def calculate(self, s: str) -> int:
        result, prev_sign, num, stack, s = 0, 1, 0, [], s + '+0'

        for c in s:
            if c.isdigit(): num = num * 10 + ord(c) - ord('0')
            elif c in ['+', '-']:
                result += prev_sign * num
                num = 0
                prev_sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(result)
                stack.append(prev_sign)
                prev_sign, result = 1, 0
            elif c == ')':
                result += prev_sign * num   # last digit inside paren
                result *= stack.pop()       # sign before paren
                result += stack.pop()       # result before paren
                num = 0
        return result


# Approach 3: 2 Stacks
# Refer to java file with same name

# 224. Basic Calculator
# https://leetcode.com/problems/basic-calculator/description/

# Example: (1+(4+5+2)-3)+(6+8) Answer = 23

# c: (
# before: num: 0 | sign: 1 | stack: [] | res: 0
# after: num: 0 | sign: 1 | stack: [0, 1] | res: 0
# c: 1
# before: num: 0 | sign: 1 | stack: [0, 1] | res: 0
# after: num: 1 | sign: 1 | stack: [0, 1] | res: 0
# c: +
# before: num: 1 | sign: 1 | stack: [0, 1] | res: 0
# after: num: 0 | sign: 1 | stack: [0, 1] | res: 1
# c: (
# before: num: 0 | sign: 1 | stack: [0, 1] | res: 1
# after: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# c: 4
# before: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# after: num: 4 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# c: +
# before: num: 4 | sign: 1 | stack: [0, 1, 1, 1] | res: 0
# after: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# c: 5
# before: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# after: num: 5 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# c: +
# before: num: 5 | sign: 1 | stack: [0, 1, 1, 1] | res: 4
# after: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# c: 2
# before: num: 0 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# after: num: 2 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# c: )
# before: num: 2 | sign: 1 | stack: [0, 1, 1, 1] | res: 9
# after: num: 0 | sign: 1 | stack: [0, 1] | res: 12
# c: -
# before: num: 0 | sign: 1 | stack: [0, 1] | res: 12
# after: num: 0 | sign: -1 | stack: [0, 1] | res: 12
# c: 3
# before: num: 0 | sign: -1 | stack: [0, 1] | res: 12
# after: num: 3 | sign: -1 | stack: [0, 1] | res: 12
# c: )
# before: num: 3 | sign: -1 | stack: [0, 1] | res: 12
# after: num: 0 | sign: -1 | stack: [] | res: 9
# c: +
# before: num: 0 | sign: -1 | stack: [] | res: 9
# after: num: 0 | sign: 1 | stack: [] | res: 9
# c: (
# before: num: 0 | sign: 1 | stack: [] | res: 9
# after: num: 0 | sign: 1 | stack: [9, 1] | res: 0
# c: 6
# before: num: 0 | sign: 1 | stack: [9, 1] | res: 0
# after: num: 6 | sign: 1 | stack: [9, 1] | res: 0
# c: +
# before: num: 6 | sign: 1 | stack: [9, 1] | res: 0
# after: num: 0 | sign: 1 | stack: [9, 1] | res: 6
# c: 8
# before: num: 0 | sign: 1 | stack: [9, 1] | res: 6
# after: num: 8 | sign: 1 | stack: [9, 1] | res: 6
# c: )
# before: num: 8 | sign: 1 | stack: [9, 1] | res: 6
# after: num: 0 | sign: 1 | stack: [] | res: 23


sol = Solution()
assert sol.calculate("1 + 1") == 2
assert sol.calculate(" 2-1 + 2 ") == 3
assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23
