# l, r counters
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        for c in s:
            if c == "(":
                l += 1
            else:
                r += 1

            if l == r:
                max_len = max(max_len, l + r)
            elif r > l:
                l = r = 0

        l, r = 0, 0
        for c in reversed(s):
            if c == "(":
                l += 1
            else:
                r += 1

            if l == r:
                max_len = max(max_len, l + r)
            elif l > r:
                l = r = 0

        return max_len


# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/description/
