from typing import List


# Approach 2: Kadane
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        cur_max, max_so_far, n = 0, 0, len(prices)

        for i in range(1, n):
            cur_max = (0, cur_max + prices[i] - prices[i - 1])
            max_so_far = max(max_so_far, cur_max)

        return max_so_far


# Approach 3: Simple One Pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit



# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# At most 1 transaction

# Time: O(n)
# Space: O(1)

# Approach 1: DP

# Approach 2: Kadane
# All the straight forward solution should work,
# but if the interviewer twists the question slightly by giving the difference array of prices,
# Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.

# Approach 3: Simple One Pass

# Steps:
# 1. We iterate through the list, keeping a running min
# 2. We caculate the profit of selling with curr price after buying at min price
# 3. We keep a running max of the max profit and return that at the end


