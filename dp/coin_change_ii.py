class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            c = coins[i - 1]
            for j in range(1, amount + 1):
                if j >= c:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - c]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][amount]


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for j in range(1, amount + 1):
                if c > j:
                    continue
                dp[j] += dp[j - c]

        return dp[amount]


# 2D
# dp[i][j] represents no. of ways we can form target j using coins[0:i]
# dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
# dp[i][0] = 1
# dp[0][j] = 0
# dp[n][amount]
