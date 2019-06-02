import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        if len(s) < len(t): return ""

        t_hash, s_hash = collections.Counter(t), collections.Counter()
        desired, formed, l, r, n = len(t_hash), 0, 0, 0, len(s)
        window = [n + 1, 0, 0] # [min_len, l, r]

        while r < n:
            rc = s[r]
            s_hash[rc] += 1

            if rc in t_hash and t_hash[rc] == s_hash[rc]: formed += 1

            while formed == desired:
                window_len = r - l + 1
                if window_len < window[0]: window = [window_len, l, r]
                lc = s[l]
                if lc in t_hash and t_hash[lc] == s_hash[lc]: formed -= 1
                s_hash[lc] -= 1
                l += 1

            r += 1

        return "" if window[0] == n + 1 else s[window[1]:window[2] + 1]

# t = a
# s = 
