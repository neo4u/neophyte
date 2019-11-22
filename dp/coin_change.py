from typing import List


# Approach 1: Backtracking
class Solution1A:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n, self.result = len(coins), float("inf")
        for i in range(n): self.dfs(coins, n, i, amount, 0)

        return -1 if self.res == float("inf") else self.res

    def dfs(self, coins, n, start, rem, count):
        if rem == 0: self.result = min(self.result, count)

        for i in range(start, n):
            if coins[i] <= rem < coins[i] * (self.result - count):
                self.dfs(coins, n, i, rem - coins[i], count + 1)


# VERY SLOW
# Approach 1: DFS
class Solution1B:
    def coinChange(self, coins, amount):
        memo = {}
        result = self.dfs(coins, amount, memo)
        return -1 if result == float('inf') else result

    def dfs(self, coins, amount, memo):
        if amount == 0: return 0
        if amount in memo: return memo[amount]

        result = float('inf')
        for coin in coins:
            if amount < coin: continue
            result = min(result, self.dfs(coins, amount - coin, memo) + 1)

        memo[amount] = result
        return result


# Approach 2: BFS
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        q, visited, distance = [0], set([0]), 0

        while q:
            level_q = []

            for node in q:
                for coin in coins:
                    nbr = node + coin
                    if amount == nbr: return distance + 1
                    if amount < nbr or nbr in visited: continue

                    visited.add(nbr)
                    level_q.append(nbr)

            q = level_q
            distance += 1

        return -1


# VERY SLOW
# Approach 3: DP 2D
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        n = len(coins)

        dp = [[amount + 1 for i in range(amount + 1)] for j in range(n + 1)]
        for i in range(n + 1): dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j < coins[i - 1]: dp[i][j] = dp[i - 1][j]
                else:   dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

        return -1 if dp[n][amount] == amount + 1 else dp[n][amount]


# Approach 4: DP 1D
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        if amount == 0: return 0

        dp = [0] + [float('inf')] * amount
        for c in coins:
            for i in range(1, amount + 1):
                if i < c: continue
                dp[i] = min(dp[i], dp[i - c] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]


# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/

# Approach 1A: Backtracking
# Approach 1B: DFS

# Approach 2: BFS

# Approach 2: DP 2D

# Time: O(amount * n)
# Space: O(amount * n)

# Approach 3: DP 1D
# Model:
# dp[i] represents fewest number of coins making up amount i

# Base Case:
# dp[0] = 0

# Transistion funciton:
# dp[i] = min of |dp[i]            | for every coin in coins
#                |dp[i - coin] + 1)|
# dp[i] here represents the fewest number of coins to form amount 'i' before the curr coin was considered
# dp[i - coin] + 1 represents the fewest number of coins to form amount 'i - curr coin value' + 1 to add the current coins
# we select whichever of these is lesser

# Time: O(amount * n)
# Space: O(amount)


# assert_equal(coin_change_bfs([186,419,83,408], 6249), 20)
# assert_equal(coin_change_bfs([1,2,5], 11), 3)
# assert_equal(coin_change_bfs([2], 3), -1)

# assert_equal(coin_change_dfs([186,419,83,408], 6249), 20)
# assert_equal(coin_change_dfs([1,2,5], 11), 3)
# assert_equal(coin_change_dfs([2], 3), -1)

# # assert_equal(coin_change_dp([186,419,83,408], 6249), 20)
# # assert_equal(coin_change_dp([1,2,5], 11), 3)
# # assert_equal(coin_change_dp([2], 3), -1)
# assert_equal(coin_change_dp([1, 2], 3), 2)
