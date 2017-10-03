# @param {Integer[][]} costs
# @return {Integer}
def min_cost(costs)
  return 0 if costs.empty?
  n = costs.size
  1.upto(n - 1) do |i|
    costs[i][0] = costs[i][0] + [costs[i - 1][1], costs[i - 1][2]].min
    costs[i][1] = costs[i][1] + [costs[i - 1][2], costs[i - 1][0]].min
    costs[i][2] = costs[i][2] + [costs[i - 1][0], costs[i - 1][1]].min
  end
  [costs[n - 1][0], costs[n - 1][1], costs[n - 1][2]].min
end

# Should be 10
puts min_cost([[17,2,17],[16,16,5],[14,3,19]])

puts min_cost([[20,18,4],[9,9,10]])
