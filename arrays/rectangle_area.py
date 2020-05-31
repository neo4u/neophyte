class Solution:
    def computeArea(self, l1: int, d1: int, r1: int, u1: int, l2: int, d2: int, r2: int, u2: int) -> int:
        first = (r1 - l1) * (u1 - d1)
        second = (r2 - l2) * (u2 - d2)

        # overlap
        l, d = max(l1, l2), max(d1, d2)
        r, u = min(r1, r2), min(u1, u2)

        width = max(r - l, 0)
        height = max(u - d, 0)
        overlap = width * height

        return first + second - overlap


# 223. Rectangle Area
# https://leetcode.com/problems/rectangle-area/description/

# Similar to 2D range sum - Immutable problem
