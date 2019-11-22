from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)

        if k >= n // 2: return self.max_profit_unltd(prices)
        dp = [[0 for _ in range(n)] for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(n):
                dp[i][j] = max(max_diff + prices[j], dp[i][j - 1])
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        return dp[k][n - 1]

    def max_profit_unltd(self, prices):
        profit, n = 0, len(prices)

        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            if diff > 0: profit += diff
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


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# 123. Best Time to Buy and Sell Stock III

# dp[i][j] represents max profit on ith transaction on jth day
# dp[0][i] = 0 Set by default at 2D array init
# dp[i][0] = 0 Set by default at 2D array init

# dp[i][j] = max { dp[i][j - 1]     Max of not tranacting today and just using previous day's profits for ith transaction
#                { prices[j] - prices[m] +  dp[i - 1][m] j = 0...j - 1
#                  prices[j] - prices[m] because to sell on day j we must have bought on day m,
#                                      so we subtract prices[j] - prices[m]
#                  plus dp[i - 1][m] because we have to add the profit from the mth day

# The second part of the equation can be summarzied
# by maintaining a local maximum for each transaction and thus it becomes
# dp[i][j] = max    { dp[i][j - 1]
#                   { prices[j] + max_diff
#  where max_diff = max { max_diff,
#                       { dp[i - 1][j] - prices[j] for j from 0 to n - 1
