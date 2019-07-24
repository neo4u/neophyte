# ust like N-queen problem, I use x,y represent the position of each grid
# all position in the same left diagonals have the same x+y
# all position in the same right diagonals have the same y-x

# so we just need to use index to judge the cell(illuminated or not)

# for example, if [1,1] is a lamp, then all x = 1 or y = 1 or x+y=2 or y-x=0 cell will be illuminated.
from collections import Counter

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        lamps = list(map(tuple, lamps))
        light_set = set(lamps)
        # one cell may be illuminated by many lamps
        rows, cols, asc_diags, dsc_diags = Counter(), Counter(), Counter(), Counter()
        for x, y in lamps:
            rows[x] += 1
            cols[y] += 1
            asc_diags[x + y] += 1
            dsc_diags[y - x] += 1

        result = []
        for x, y in queries:
            # Append answer to query in result
            if x in rows or y in cols or x + y in asc_diags or y - x in dsc_diags:
                result.append(1)
            else:
                result.append(0)

            # Turn of the lamp and reduce the illumination by the light to 8 nbrs
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]:
                r, c = x + dx, y + dy
                if (r, c) not in light_set: continue

                light_set.remove((r, c))
                rows[r] -= 1
                if rows[r] == 0: del rows[r]

                cols[c] -= 1
                if cols[c] == 0: del cols[c]

                asc_diags[r + c] -= 1
                if asc_diags[r + c] == 0: del asc_diags[r + c]

                dsc_diags[c - r] -= 1
                if dsc_diags[c - r] == 0: del dsc_diags[c - r]

        return result


# 1001. Grid Illumination
# https://leetcode.com/problems/grid-illumination/description/
