import collections

class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or len(s1) > len(s2): return False

        s1_hash = collections.Counter(s1)
        m, n, desired, formed = len(s1), len(s2), len(s1_hash), 0
        s_hash = collections.defaultdict(int)

        for j in range(m):
            c = s2[j]
            s_hash[c] += 1
            if c in s1_hash and s1_hash[c] == s_hash[c]: formed += 1
        if formed == desired: return True

        r = m
        while r < n:
            l = r - m + 1
            out_c, in_c = s2[l - 1], s2[r]

            if out_c in s1_hash and s1_hash[out_c] == s_hash[out_c]: formed -= 1
            s_hash[out_c] -= 1

            s_hash[in_c] += 1
            if in_c in s1_hash and s1_hash[in_c] == s_hash[in_c]: formed += 1

            if formed == desired: return True
            r += 1

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        d1, d2 = collections.Counter(s1), collections.Counter(s2[:m])
        if d1 == d2: return True

        for i in range(m, n):
            out_c, in_c = s2[i - m], s2[i]
            d2[out_c] -= 1; d2[in_c] += 1
            if d2[out_c] == 0: d2.pop(out_c)
            if d1 == d2: return True

        return False




# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
