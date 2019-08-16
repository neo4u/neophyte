from typing import List
import heapq

class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        m, n = len(grid), len(grid[0])
        heap, visited = [], set()

        # Next two loops are for, put surrounding heights into heap
        for i in [0, m - 1]: # First put top and bottom most row
            for j in range(n):
                heap.append((grid[i][j], i, j))
                visited.add((i, j))

        for j in [0, n - 1]: # then put first and last column
            for i in range(m):
                if (i, j) in visited: continue
                heap.append((grid[i][j], i, j))
                visited.add((i, j))

        heapq.heapify(heap)
        dirs, ans = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0

        while heap:
            h, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                r, c = x + dx, y + dy
                if not self.valid(m, n, r, c, visited): continue
                ans += max(0, h - grid[r][c])
                itm = (max(h, grid[r][c]), r, c)
                heapq.heappush(heap, itm)
                visited.add((r, c))

        return ans

    def valid(self, m, n, x, y, visited):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1 and (x, y) not in visited

# 407. Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/description/

# Steps:
# 1. First we add all the surrounding to the building heights to a min_heap. Why?
#    Cuz we want to get the building that decides the level of the water that is held within
# 2. We pop from the min_heap, to get the least height building, this dictates how much water to add to result/ans
# 3. For each neighbour of the popped height we can get different in height and add that difference to the answer, as long as that is +ve
# 4. And then we push the (max(h, height of nbr), r, c), why? The max height dictates how much water will stay for (r, c) nbrs,
#    so if (r, c) is higher than the max so far, then that (r, c) will dictate how much it's nbrs can hold, so we pass the max along
# 5. Also, we use the visited array to keep track of all the visited co-ordinates and only visit unvisited nbrs

# Time: O(m * n log(m * n))
# Space: O(m * n)


# [[7, 1, 7, 7, 7],
#  [7, 2, 3, 4, 7],
#  [1, 7, 7, 7, 7]]


# 9 9 9 9 9 9 9 9 9 9
# 9   1 1           9
# 9   7 7 7 7 7 7 1 9
# 9   7         7 1 9
# 9   7 7 7 7 7 7 1 9
# 9                 9
# 9 9 9 9 9 9 9 9 9 9 

# 7 7 7 7 7 7 7 7 7 7
# 7 1 7 1 1 1 1 1 1 7
# 7 1 9 9 9 9 9 1 7 7
# 7 1 9 2 2 2 2 9 1 7
# 7 1 9 9 9 9 9 9 1 7
# 7 1 1 1 1 1 1 1 1 7
# 7 7 7 7 7 7 7 7 7 7

#  [[7, 1, 7, 7, 7],
#  [7, 2, 3, 4, 7],
#  [1, 7, 7, 7, 7]]
