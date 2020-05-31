from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(A), len(B)
        result = []

        while i < m and j < n:
            a1, a2 = A[i]
            b1, b2 = B[j]

            if self.has_overlap(a1, a2, b1, b2):
                intersect = [max(a1, b1), min(a2, b2)]
                result.append(intersect)

            if a2 < b2:     i += 1 # A[i] ends first so advance i, since we've counted its intersection upto a2
            elif b2 < a2:   j += 1 # B[j] ends first so advance j, since we've counter its intersection upto b2
            else:
                i += 1; j += 1

        return result

    def has_overlap(self, a1, a2, b1, b2):
        return b1 <= a1 <= b2 or a1 <= b1 <= a2


# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/description/


# Intuition

# I. There are 3 CASES
#    1. No Overlap neither b1 <= a1 <= b2 NOR a1 <= b1 <= a2
#    a1------a2
#                b1-------b2
#    2. a1 between b1 and b2
#            a1-------a2
#        b1---------------b2
#    3. b1 between a1 and b2
#        a1------------a2
#                b1---------------b2
# II. Another important point is that the intervals within A and B are already sorted.

# Steps:
# 1. Use 2 pointers i and j to mark the current interval in A and B
# 2. Use has_overlap to check if there is an overlap
# 3. If there is an overlap, get the intersection and insert that into result
# 4. Based on which interval amongst A[i] and B[j] ends first we advance i or j respectively,
#    this is because, we have to ensure that the (i + 1)th or (j + 1)th interval might still have an
#    intersection with the jth or ith interval respectively

# Time: O(n)
# Space: O(1)

sol = Solution()
assert sol.intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]]
) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
