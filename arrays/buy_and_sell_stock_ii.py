from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, profit = len(prices), 0

        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            if diff > 0: profit += diff

        return profit


# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

# Approach 1: Use all the Peaks
# Steps:
# 1. We iterate through the list
# 2. Whenever, we see there is a hill, prev < curr, we add the difference to the profit,
#    meaning that we sell every time there is a rise in prices of the stock, which makes sense
