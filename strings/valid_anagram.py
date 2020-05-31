class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n: return False

        a1, a2 = [0] * 26, [0] * 26
        for i in range(n):
            a1[ord(s[i]) - ord('a')] += 1
            a2[ord(t[i]) - ord('a')] += 1

        return a1 == a2


import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = collections.Counter(s)
        for c in set(t):
            c1 = counts.get(c)
            if not c1: return False
            c2 = t.count(c)
            if c1 != c2: return False

        return True


# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
