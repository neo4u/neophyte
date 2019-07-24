class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        if k >= n // 2: return self.max_profit_unlimited_transactions(prices)
        dp = [[0 for j in range(n)] for i in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]

    def max_profit_unlimited_transactions(self, prices):
        profit, n = 0, len(prices)

        for i in range(1, n):
            if prices[i] <= prices[i - 1]: continue
            profit += prices[i] - prices[i - 1]

        return profit

# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

# dp[i][j] represents ith transaction on jth day
# dp[0][j], dp[i][0] = 0
# recurrence relation
# dp[i][j] = max(transact today or don't)
#            max { dp[i][j - 1]
#                { max_diff + prices[j]
# where max_diff = max { dp[i - 1][m] - prices[m] for all m from 0 to j - 1
