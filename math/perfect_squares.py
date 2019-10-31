import math


# Approach 1: Brute Force
class Solution1:
    def numSquares(self, n: int) -> int:
        upper = int(math.sqrt(n))
        self.square_nums = [i**2 for i in range(1, upper + 1)]
        return self.recurse(n)

    def recurse(self, k):
        if k in self.square_nums: return 1  # bottom cases: find a square number
        min_num = float('inf')

        for sq in self.square_nums:     # Find the minimal value among all possible solutions
            if k < sq: break
            new_num = self.recurse(k - sq) + 1
            min_num = min(min_num, new_num)

        return min_num


# Approach 2: DP, TLE on OJ
class Solution2:
    def numSquares(self, n: int) -> int:
        upper = int(math.sqrt(n))
        square_nums = [i**2 for i in range(1, upper + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # base case

        for i in range(1, n + 1):
            for sq in square_nums:
                if i < sq: break
                dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]


# Approach 3: BFS
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 0: return
        if n == 0: return 1

        upper = int(math.sqrt(n))
        squares = [i**2 for i in range(1, upper + 1)]

        # Mark the distance at 0 as 1
        q, visited, distance = [0], set([0]), 0
        while q:
            level_q = []

            for node in q:
                for square in squares:
                    tmp = square + node
                    if tmp == n: return distance + 1    # Return the distance at current node, +1 to account for the curr neighbor
                    if tmp > n: break                   # We only add neighbours which are less than n

                    if tmp in visited: continue         # Skip already considered sums of squares
                    visited.add(tmp)

                    level_q.append(tmp)                 # Add to queue and increment the distance of current level by 1

            q = level_q
            distance += 1


# Approach 4: Math
class Solution4:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq * sq == n

    def numSquares(self, n: int) -> int: # Lagrange's four-square theorem
        if self.isSquare(n): return 1

        while (n & 3) == 0: n >>= 2
        if (n & 7) == 7: return 4
        sq = int(math.sqrt(n)) + 1

        for i in range(1, sq):
            if self.isSquare(n - i * i): return 2

        return 3


# 279.Perfect Squares
# https://leetcode.com/problems/perfect-squares/description/


# Approach 1: Brute-Force, Recursive
# Visits many nodes at the same time

# Approach 2: DP
# dp[i] represents the min no. of squares to form sum i
# Base case
# dp[0] = 0
# dp[i] = min(dp[n - k] + 1) for all k, where k is a square number in range [1, sqrt(n)]
# dp[n - k] represents, the min squares required to form sum (n - k) + 1 more square number which is k
# dp[n] is what we need.

# Approach 3: Greedy Enumeration

# Approach 4: Greedy + BFS

# Intuition:
# 1. We can view this as a graph question if we treat each number from 1 to n as nodes.
# 2. There is an edge between two nodes i and j if and only if there exists a number k such that:
#    i = j + k * k or j = i + k * k, where k * k ≤ i and k*k ≤ j
# 3. Since BFS ensures that we get the shortest path, we can get the minimum no. of squares to get sum n

# Time: O(n+*h/2), where h is the height of the n-ary tree
# Space: O(n+*h/2)


# Approach 4: Math


sol = Solution()
assert sol.numSquares(12) == 3
assert sol.numSquares(7168) == 4
