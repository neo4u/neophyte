import re

# Approach 1: Regex and Stack
class Solution:
    def arithmetic(self, res, op, num):
        if not op:
            res = num
        else:
            res += num * [-1, 1][(op == "+") * 1]
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
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            print(f"c: {c}")
            print(f"before: num: {num} | sign: {sign} | stack: {stack} | res: {res}")
            if c.isdigit():
                num = 10*num + int(c)       # calculate the full digit, so add c at 10s digts to current num
            elif c in ["-", "+"]:
                res += sign*num
                num = 0                     # reset the num variable to 0 for next digit
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
            print(f"after: num: {num} | sign: {sign} | stack: {stack} | res: {res}")

        return res + num*sign


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
# assert sol.calculate("1 + 1") == 2
assert sol.calculate(" 2-1 + 2 ") == 3
# assert sol.calculate("(1+(4+5+2)-3)+(6+8)") == 23
