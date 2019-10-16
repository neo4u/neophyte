# Approach 1: Stack
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l, r = 0, 0

        for c in S:
            if c == '(':    l += 1
            elif l > 0:     l -= 1
            else:           r += 1

        return l + r


# Faster ruby specific version
# @param {String} s
# @return {Integer}
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while '()' in S: S = S.replace('()', '')

        return len(S)


# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
