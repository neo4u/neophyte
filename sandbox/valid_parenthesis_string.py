class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0

        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1

            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0

# ()(((*)
# l  h
# 1  1
# 0  0
# 1  1
# 2  2
# 3  3
# 2  4
# 1  3
# invalid cuz l == 0 is false


# ()((**)
# l   r
# 1   1
# 0   0
# 1   1
# 2   2
# 1   3
# 0   4
# -1  3
# 0   3

class Solution:

    def checkValidString(self, s):
        stack = []
        for c in s:
            if c in '(*':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

        stars = []
        open_parens = []
        for i, c in enumerate(stack):
            if c == '*':
                stars.append(i)
            elif c == '(':
                open_parens.append(i)
            else:  # c == ')'
                if open_parens:
                    open_parens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while open_parens:
            i = open_parens.pop()
            if not stars:
                return False
            if stars[-1] < i:
                return False
            stars.pop()

        return True
