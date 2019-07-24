import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        result = []
        heights = []
        for s, e, h in buildings:
            heights.append((s, -h))
            heights.append((e, h))

        heights = sorted(heights)
        pq, prev = [0], 0

        # [(5, -1000), (5, -20), (7, -25), (19, 25), (20, -20), (20, 20), (20, 1000), (30, 20)]
        # pq    : [0]
        # result: [(5, 1000), (20, 20), (30, 0)]
        for h in heights:
            if h[1] < 0:
                heapq.heappush(pq, h[1])
            else:
                pq.remove(-h[1])
                heapq.heapify(pq)

            cur = -pq[0]
            if prev != cur:
                result.append([h[0], cur])
                prev = cur

        return result


# 218. The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/description/

# Algorithm
# 1. Build a hash called height_map which records the "heights" (keys) and number of same "height" values
# 2. Build an array of points , which seaprates out the lef-edge of the building with height (by negating the height value) and right-edge and height (positive value)
# 3. For each point, the max height is got by the keys and checking the current height and previous height 
# 4. Retain if same value is not repeated

# Example:
# chipotle, empire state and mcDonalds with same or different height
# [[5, 20, 1000], [5, 20, 20], [7, 19, 25], [20, 30, 20]]
# [(5, -1000), (20, 1000), (5, -20), (20, 20), (7, -25), (19, 25),(20, -20), (30, 20)]
# sorted: [(5, -1000), (5, -20), (7, -25), (19, 25), (20, -20), (20, 20), (20, 1000), (30, 20)]

sol = Solution()
assert sol.getSkyline([[5, 20, 1000], [5, 20, 20], [7, 19, 25], [20, 30, 20]]) == [[5, 1000], [20, 20], [30, 0]]
assert sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
assert sol.getSkyline([]) == []
assert sol.getSkyline([[0, 1, 3]]) == [[0, 3],[1, 0]]
assert sol.getSkyline([[0, 2147483647, 2147483647]]) == [[0, 2147483647], [2147483647, 0]]
assert sol.getSkyline([[0, 2, 3],[2, 5, 3]]) == [[0, 3], [5, 0]]
