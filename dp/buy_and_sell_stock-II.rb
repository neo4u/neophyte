# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  profit = 0
  1.upto(n - 1) do |c|
    profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1]
  end
  profit
end
