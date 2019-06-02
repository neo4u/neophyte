class Solution:
    def isIsomorphic(self, s, t):
        m, n = len(s), len(t)
        if m != n: return False

        map1, map2 = {}, {}
        for i in range(m):
            c1, c2 = s[i], t[i]

            if c1 not in map1:
                map1[c1] = c2
            else:
                if map1[c1] != c2: return False

            if c2 not in map2:
                map2[c2] = c1
            else:
                if map2[c2] != c1: return False

        return True