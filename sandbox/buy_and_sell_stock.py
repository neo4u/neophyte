class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price, max_profit, n = prices[0], 0, len(prices)

        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                max_profit = max(max_profit, profit)

        return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n, profit = len(prices), 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
