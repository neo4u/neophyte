# @param {Integer} k
# @param {Integer[]} prices
# @return {Integer}
def max_profit(k, prices)
	return 0 if k.zero? || prices.empty?
	n = prices.size
	return max_profit_unlimited_transactions(prices) if k >= n / 2
	dp = Array.new(k + 1) { Array.new(n, 0) }
	# dp[i][j] represents max profit on ith transaction on jth day
	# dp[0][i] = 0
	# dp[i][0] = 0
	# dp[i][j] = max { dp[i][j - 1] }
	#  				 { price[j] - price[m] +  dp[i - 1][j] 0...n - 1}

	1.upto(k) do |i|
		max_diff = -prices[0]

		1.upto(n - 1) do |j|
			# Max of not tranacting today and just using previous day's profits or
			# transacting and adding to previous day's profits
			dp[i][j] = [dp[i][j - 1], prices[j] + max_diff].max

			# Profit from last transaction minus price from today. Local maximum for jth day
			max_diff = [max_diff, dp[i - 1][j] - prices[j]].max
		end
	end

	dp[k][n - 1]
end

def max_profit_unlimited_transactions(prices)
	profit, n = 0, prices.size

	1.upto(n - 1) do |i|
		profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1]
	end

	profit
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(max_profit(2, [1]), 0)
assert_equal(max_profit(2, [2,4,1]), 2)
assert_equal(max_profit(2, [3,2,6,5,0,3]), 7)
