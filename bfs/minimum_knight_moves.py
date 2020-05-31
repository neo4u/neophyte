
# Approach 1: With only making abs for x, y, This is SLOW but passes
class SolutionBFS1:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        q, visited = [(0, 0)], set([(0, 0)])
        dirs = [
            (-2, 1), (-1, 2), (1, 2), (2, 1), 
            (2, -1), (1, -2), (-1, 2), (-2, -1)
        ]
        dist = 0

        while q:
            level_q = []
            for node in q:
                curr_x, curr_y = node
                if (curr_x, curr_y) == (x, y): return dist
                for dx, dy in dirs:
                    nx, ny = (curr_x + dx, curr_y + dy)
                    if (nx, ny) == (x, y): return dist + 1

                    if (nx, ny) in visited: continue
                    visited.add((nx, ny))
                    level_q.append((nx, ny))

            q = level_q
            dist += 1

        return -1


# Approach 1: With enforcing only first quadrant check, Little FASTER
class SolutionBFS:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0: return 0
        x, y = abs(x), abs(y)
        level = 1
        q, visited = [(0, 0)], set([(0, 0)])
        dirs = [
            (-2, 1), (-1, 2), (1, 2), (2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        while q:
            level_q = []
            for cx, cy in q:
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) == (x, y): return level

                    if (nx, ny) in visited or nx < -1 and ny < -1: continue
                    visited.add((nx, ny))
                    level_q.append((nx, ny))

            q = level_q
            level += 1

        return -1



# Approach 2: A*, Quick FAST
from collections import deque
from heapq import heappush, heappop

MOVES = [
    (-2, -1), (-2, 1),
    (-1, 2), (1, 2),
    (2, 1), (2, -1),
    (-1, -2), (1, -2)
]


class SolutionAStar:
    def minKnightMoves(self, targetx: int, targety: int) -> int:
        # The heuristic function returns the sum of the number of moves to get to
        # the position and weighted manhattan distance to the target position.
        # The coefficient for manhattan distance was picked experimentally:
        # the bigger the coefficient - the bigger the impact of the distance to the
        # decision of selecting next expanded move from the frontier
        # We want the number of moves to have a bigger weight in order to reach the
        # target position in the minimum number of steps possible.
        def heuristic(moves, x, y):
            return moves + 0.3333 * (abs(x - targetx) + abs(y - targety))

        # helper funtion to push a potential state to the frontier
        def add_to_q(q, x, y, moves):
            score = heuristic(moves, x, y)
            heappush(q, (score, moves, x, y))

        # keep track of the visited positions
        visited = {(0, 0)}

        # a min-priority queue for holding next moves as a min-priority queue with tuples
        # format: (<score>, <moves>, <x>, <y>)
        q = []

        # add initial position to the frontier
        add_to_q(q, 0, 0, 0)

        # expand frontier one move at a time
        while q:
            _, moves, x, y = heappop(q)  # 'best' move getting selected
            if x == targetx and y == targety:
                return moves

            for dx, dy in MOVES:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in visited: continue
                visited.add((new_x, new_y))
                add_to_q(q, new_x, new_y, moves + 1)

        return -1


# Approach 3: Recursive DP with memoization, FASTEST SOLUTION
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        self.cache = {}
        return self.dfs(x, y)

    def dfs(self, x, y):
        if (x, y) in self.cache: return self.cache[(x, y)]
        x, y = abs(x), abs(y)
        if x == y == 0: return 0
        if x + y == 2: return 2
        result = min(self.dfs(x - 1, y - 2), self.dfs(x - 2, y - 1)) + 1
        self.cache[(x, y)] = result

        return result


# Approach 1: BFS with pruning

# Pruning Criteria:
# 1. Use 1st Quadrant only
# 2. Use manhattan distance or each new node with dst and curr node with dst,
#    use the one that can move closer to dst than curr node
# https://leetcode.com/problems/minimum-knight-moves/discuss/452653/Python-Passed-BFS-with-heuristic


# Approach 2: A*, Dijstras with complex heuristic for heap order,
# (Not ideal for interviews), but just for learning
# https://leetcode.com/problems/minimum-knight-moves/discuss/389288/A*-search-a-variant-of-Dijkstra

# ***BEST SOLUTION***
# https://leetcode.com/problems/minimum-knight-moves/discuss/482507/A*-solution-(no-symmetry-no-math-no-DP)

# Approach 3: DP (Top-Down DP with memoization) Easiest for interview
# Recurrence relation
# resulft for (x, y) = min(result for (x - 1, y - 2), result for (x - 2, y - 1))
