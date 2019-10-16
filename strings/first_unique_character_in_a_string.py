import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)

        for i, c in enumerate(s):
            if c in counts and counts[c] == 1: return i

        return -1
