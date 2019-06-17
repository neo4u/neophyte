import collections
import itertools

class Solution(object):
    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)
        lastx = {}
        res = float("inf")

        for x in sorted(p):
            p[x].sort()
            for y1, y2 in itertools.combinations(p[x], 2):
                if (y1, y2) not in lastx: continue
                res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                lastx[y1, y2] = x
        return res if res < float("inf") else 0


# 939. Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/description/
