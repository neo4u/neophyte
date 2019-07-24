class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[amount + 1 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        return -1 if dp[n][amount] == amount + 1 else dp[n][amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for c in coins:
            for j in range(1, amount + 1):
                if j < c: continue
                dp[j] = min(dp[j], 1 + dp[j - c])

        return -1 if dp[amount] == float('inf') else dp[amount]


# 2D
# dp[i][j] represents min no. of coins required to form target j with i denominations of coins

# dp[i][j] = min(dp[i - 1][j], dp[i][j - nums[i - 1]] + 1)
# min of:
# 1. min coins to form amount j with i - 1 denominations
# 2. min coins to form amount j - coin value with i denominations

# dp[0][0] = 0
# dp[i][0] = 0
# dp[0][j] = inf

# dp[n][amount]


# 1D
# dp[i] fewest coins to form target i
# dp[i] = min(dp[i], 1 + dp[i - coin]) for all coins
# dp[0] = 0
# dp[amount] is the answer
