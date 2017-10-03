# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  max, min = 0, Float::INFINITY
  prices.each do |c|
    min = [min, c].min
    max = [max, c - min].max
  end
  max
end
