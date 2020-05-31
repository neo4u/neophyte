import collections
import itertools


class Solution:
    def minAreaFreeRect(self, points):
        points = [complex(x, y) for x, y in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))

        return ans if ans < float("inf") else 0


# 963. Minimum Area Rectangle II
# https://leetcode.com/problems/minimum-area-rectangle-ii/description/
