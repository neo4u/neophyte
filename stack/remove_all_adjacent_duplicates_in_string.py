# Approach 1: cc replacements
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}

        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')

        return S


# Approach 2: Stack
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for c in S:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

# Approach 1: cc Replacements
# Approach 2: Stack

# Time: O(n)
# Space: O(n)
