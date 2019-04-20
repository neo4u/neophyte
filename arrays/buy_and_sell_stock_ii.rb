# @note Using peak and valley summation
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    i, max_profit = 0, 0
    while i < prices.length - 1
        i += 1 until i >= prices.length - 1 || prices[i] < prices[i + 1]
        valley = prices[i]
        i += 1 until i >= prices.length - 1 || prices[i] > prices[i + 1]
        peak = prices[i]
        max_profit += peak - valley
    end

    max_profit
end

# @note Using profit aggregation
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    profit = 0
    1.upto(prices.length - 1) do |i|
        profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1]
    end

    profit
end

# @note Using Dynamic programming
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    return 0 if prices.empty?
    n = prices.size
    max_profit = 0
    dp_sell = Array.new(n, 0) # dp_sell for profits on day i before purchase
    dp_buy = Array.new(n, 0) # dp_buy for profits on day i after purchase

    # dp_sell[i] = max(dp1[i-1]+price[i],dp_sell[i-1]) --> Sell on day i or do nothing
    # dp_buy[i] = max(dp_sell[i-1])-price[i],dp_buy[i-1]) --> Buy on day i or do nothing
    # dp_sell[0] = 0, dp_buy[0]=-Float::INFINITY (Least number)
    # before purchase on day 0 u've no profit or loss,
    # after purchase on day 0 u've negative amounts obviously
    dp_sell[0], dp_buy[0] = 0, -prices[0]

    1.upto(n - 1) do |i|
        dp_sell[i] = [dp_buy[i - 1] + prices[i], dp_sell[i - 1]].max
        dp_buy[i] = [dp_sell[i - 1] - prices[i], dp_buy[i - 1]].max
        max_profit = [max_profit, dp_sell[i]].max
        max_profit = [max_profit, dp_buy[i]].max
        puts max_profit
    end

    max_profit
end


# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Unimited transactions

# 1. DP

# 2. Simple One Pass
# Steps
# - For every day check if today's price > y'day's price
# - If yes, then sell and add to profit

# Time: O(n)
# Space: O(1) for 1 pass, O(n) for dp.

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_profit([7,1,5,3,6,4]), 7)
assert_equal(max_profit([1,2,3,4,5]), 4)
assert_equal(max_profit([7,6,4,3,1]), 0)
assert_equal(max_profit([]), 0)

