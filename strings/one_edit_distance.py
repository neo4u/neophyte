class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n: s, t, m, n = t, s, n, m

        if s == t: return False
        if n - 1 > m: return False              # If they differ by more than 1 char, return false

        for i in range(m):
            if s[i] == t[i]: continue
            if m == n:
                return s[i + 1:] == t[i + 1:]   # Replaceable
            else:
                return s[i:] == t[i + 1:]       # Deleteable

        return True


# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/description/
