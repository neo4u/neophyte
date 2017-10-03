# @param {Integer} k
# @param {Integer[]} prices
# @return {Integer}
def max_profit(k, prices)
  return 0 if k.zero? || prices.empty?
  days = prices.size
  return max_profit_high_k(prices) if k >= days / 2
  dp = Array.new(k + 1) { [0] * days }

  1.upto(k) do |i|
    max_diff = -Float::INFINITY
    1.upto(days - 1) do |j|
      # Profit from last transaction from the day before
      max_diff = [max_diff, dp[i - 1][j - 1] - prices[j - 1]].max
      # Max of not tranacting today and just using previous day's profits or
      # transacting and adding to previous day's profits
      dp[i][j] = [dp[i][j - 1], prices[j] + max_diff].max
    end
  end

  dp[k][days - 1]
end

def max_profit_high_k(prices)
  profit, n = 0, prices.size
  1.upto(n - 1) do |i|
    profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1]
  end
  profit
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_profit(2, [1]), 0)