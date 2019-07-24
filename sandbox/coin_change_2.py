class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for j in range(1, amount + 1):
                if c > j: continue
                dp[j] += dp[j - c]
        return dp[amount]


# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/

# dp[i] = no. of ways to form amount i with all coins
# dp[i] = dp[i] + d[i-c] for every coin value 'c'
# dp[0] = 1
