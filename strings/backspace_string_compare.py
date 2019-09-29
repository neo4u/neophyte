class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.build(S) == self.build(T)

    def build(self, s):
        final_s = []
        for c in s:
            if c != "#":
                final_s.append(c)
            else:
                if final_s: final_s.pop()

        return final_s

# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/description/