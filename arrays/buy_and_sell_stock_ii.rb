# @note Using peak and valley summation
# @param {Integer[]} prices
# @return {Integer}

# def max_profit(prices)
#   i, max_profit = 0, 0
#   while i < prices.length - 1
#     i += 1 until i >= prices.length - 1 || prices[i] < prices[i + 1]
#     valley = prices[i]
#     i += 1 until i >= prices.length - 1 || prices[i] > prices[i + 1]
#     peak = prices[i]
#     max_profit += peak - valley
#   end

#   max_profit
# end

# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# @note Using profit aggregation
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  max_profit = 0
  1.upto(prices.length - 1) do |i|
    max_profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1]
  end

  max_profit
end

# puts "profit: #{profit} | loss: #{loss}"

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_profit([1,2]), 1)
