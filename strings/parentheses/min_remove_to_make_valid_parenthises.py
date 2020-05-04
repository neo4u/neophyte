class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rm_idxs, stack = set(), []

        for i, c in enumerate(s):
            if c not in '()': continue
            if c == '(':
                stack.append(i)
            elif not stack:
                rm_idxs.add(i)
            else:
                stack.pop()
        rm_idxs = rm_idxs.union(set(stack))
        valid_s = ""

        for i, c in enumerate(s):
            if i in rm_idxs: continue
            valid_s += c
        return valid_s


class Solution:
    def minRemoveToMakeValid(self, s):
        out = []
        l, r, n = 0, 0, len(s)
        include = [True] * len(s)

        for i in range(n):
            c = s[i]
            if c == '(':     l += 1
            elif c == ')':   r += 1

            if r > l:
                l, r = 0, 0
                include[i] = False

        l, r = 0, 0
        for i in reversed(range(n)):
            c = s[i]
            if c == '(':     l += 1
            elif c == ')':   r += 1

            if l > r:
                l, r = 0, 0
                include[i] = False

            if include[i]: out.append(s[i])

        return reversed(out)

# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/


# Approach 1: Use stack
# Approach 2: Using 