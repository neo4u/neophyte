import collections
class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        m, n = len(grid), len(grid[0])
        min_step = float('inf')
        hit = [[0 for _ in range(n)] for _ in range(m)]
        num_step = [[0 for _ in range(n)] for _ in range(m)]
        
        # count the number of buildings
        num_building = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_building += 1
        print(f"num_bs: {num_building}")
        # bfs
        def bfs(start_x, start_y, m, n):
            count = 1
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[start_x][start_y] = True
            queue = collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for d in directions:
                    i, j = x + d[0], y + d[1]
                    if 0 <= i < m and 0 <= j < n and visited[i][j] == False:
                        visited[i][j] = True
                        if grid[i][j] == 0:
                            queue.append((i, j, dist + 1))
                            num_step[i][j] += dist + 1
                            hit[i][j] += 1
                        elif grid[i][j] == 1:
                            count += 1
            return count == num_building

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i, j, m, n):
                        return -1
        print("c")
        print_matrix(hit)
        print("d")
        print_matrix(num_step)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and hit[i][j] == num_building:
                    min_step = min(min_step, num_step[i][j])
                else:
                    print(f"c[i][j]: {hit[i][j]} num_buildings: {num_building}")
                    
        return min_step if min_step != float('inf') else -1

def print_matrix(matrix):
    for a in matrix:
        print(a)
    print("\n")


# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# 317. Shortest Distance from All Buildings

# Key Insights
# 1. We want to build a house on a 0 point
# 2. We want to reach ALL the 1 points
# 3. We want to choose a 0 point that has the least total distance to all such points


# Approach 1: BFS from each building
# Steps:
# 1. Perform BFS from each building to each 0 
#    and keep as a matrix of sum of distances,
#    then calculate min of them all
# 2. prune bfs for nodes which will not result in small

# Time:  O(k * m * n), k is the number of the buildings or O(m^2.n^2)
# Space: O(m * n)

# A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached.
# If count1 < buildings then we know not all 1 grids are connected so we can return -1 immediately,
# which greatly improved speed (beat 100% submissions).

sol = Solution()
assert sol.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]) == 7
# assert sol.shortestDistance([[1]]) == -1
# assert sol.shortestDistance([[1,1]]) == -1
# assert sol.shortestDistance([[1],[1]]) == -1
# assert sol.shortestDistance([[1,2,0]]) == -1
# assert sol.shortestDistance([[1],[2],[0]]) == -1

# assert sol.shortestDistance([[1,0]]) == 1
# assert sol.shortestDistance([[1],[0]]) == 1
# assert sol.shortestDistance([[1,0,1]]) == 2
# assert sol.shortestDistance([[1],[0],[1]]) == 2
# assert sol.shortestDistance([[1,0],[0,1]]) == 2
# assert sol.shortestDistance([[2,0,0],[0,1,0],[1,0,0]]) == 2
# assert sol.shortestDistance([[1,2,0],[0,0,0],[0,0,0]]) == 1
# assert sol.shortestDistance([[0,2,1],[1,0,2],[0,1,0]]) == -1

# assert sol.shortestDistance([[1,1],[0,1]]) == -1
# assert sol.shortestDistance([[1,0,1,0,1]]) == -1
# assert sol.shortestDistance([[1],[0],[1],[0],[1]]) == -1
# assert sol.shortestDistance([
#     [1,1,1,1,1,0],
#     [0,0,0,0,0,1],
#     [0,1,1,0,0,1],
#     [1,0,0,1,0,1],
#     [1,0,1,0,0,1],
#     [1,0,0,0,0,1],
#     [0,1,1,1,1,0]
# ]) == 88
# assert sol.shortestDistance([
#     [1,1,1,1,1,1,1,0],
#     [0,0,0,0,0,0,0,1],
#     [0,1,1,1,1,0,0,1],
#     [1,0,0,0,0,1,0,1],
#     [1,0,0,1,0,1,0,1],
#     [1,0,1,0,0,1,0,1],
#     [1,0,0,1,1,0,0,1],
#     [1,0,0,0,0,0,0,1],
#     [0,1,1,1,1,1,1,0]
# ]) == 226
