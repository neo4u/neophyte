from typing import List
import heapq

class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        m, n = len(grid), len(grid[0])
        heap, visited = [], set()

        # init , put surrounding into heap
        for i in [0, m - 1]:
            for j in range(n):
                heap.append((grid[i][j], i, j))
                visited.add((i, j))

        for j in [0, n - 1]:
            for i in range(m):
                if (i, j) in visited: continue
                heap.append((grid[i][j], i, j))
                visited.add((i, j))

        heapq.heapify(heap)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans, mx = 0, float('-inf')

        while heap:
            h, x, y = heapq.heappop(heap)
            mx = max(h, mx)

            for dx, dy in dirs:
                r, c = x + dx, y + dy
                if not self.valid(m, n, r, c, visited): continue

                if mx > grid[r][c]:
                    ans += mx - grid[r][c]

                itm = (grid[r][c], r, c)
                heapq.heappush(heap, itm)
                visited.add((r, c))

        return ans

    def valid(self, m, n, x, y, visited):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1 and (x, y) not in visited


class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        m, n = len(grid), len(grid[0])
        heap, visited = [], set()

        # init , put surrounding into heap
        for i in [0, m - 1]:
            for j in range(n):
                heap.append((grid[i][j], i, j))
                visited.add((i, j))

        for j in [0, n - 1]:
            for i in range(m):
                if (i, j) in visited: continue
                heap.append((grid[i][j], i, j))
                visited.add((i, j))

        heapq.heapify(heap)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0

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