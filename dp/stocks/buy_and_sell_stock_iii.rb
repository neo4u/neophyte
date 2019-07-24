# @param {Integer} k
# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    k = 2
    return 0 if k.zero? || prices.empty?
    n = prices.size
    dp = Array.new(k + 1) { Array.new(n, 0) }

    1.upto(k) do |i|
        max_diff = -prices[0]
        1.upto(n - 1) do |j|
            dp[i][j] = [dp[i][j - 1], prices[j] + max_diff].max
            # Local maximum for the variable part of recurrence relation for ith transaction
            max_diff = [max_diff, dp[i - 1][j] - prices[j]].max
        end
    end

    dp[k][n - 1]
end

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# 123. Best Time to Buy and Sell Stock III

# Do the below and set k = 2
# dp[i][j] represents max profit on ith transaction on jth day
# dp[0][i] = 0 Set by default at 2D array init, 0 transactions, 0 profit
# dp[i][0] = 0 Set by default at 2D array init, can't complete transaction with 1 day

# recurrence
# dp[i][j] = max { dp[i][j - 1]     Max of not transacting today and just using previous day's profits for ith transaction
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

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_profit([1]), 0)
assert_equal(max_profit([2,4,1]), 2)
assert_equal(max_profit([3,2,6,5,0,3]), 7)
