import collections

class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        if not p or len(p) > len(s): return False

        p_hash = collections.Counter(p)
        m, n, desired, formed = len(s), len(p), len(p_hash), 0
        s_hash = collections.defaultdict(int)

        for j in range(n):
            c = s[j]
            s_hash[c] += 1
            if c in p_hash and p_hash[c] == s_hash[c]:
                formed += 1
        if formed == desired: return True

        r = n
        while r < m:
            l = r - n + 1
            lc, rc = s[l - 1], s[r]

            if lc in p_hash and p_hash[lc] == s_hash[lc]: formed -= 1
            s_hash[lc] -= 1

            s_hash[rc] += 1
            if rc in p_hash and p_hash[rc] == s_hash[rc]:
                formed += 1

            if formed == desired: return True
            r += 1

        return False


# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/
