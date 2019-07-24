class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        k = 2
        n = len(prices)
        dp = [[0 for j in range(n)] for i in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]
