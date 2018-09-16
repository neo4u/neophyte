# @param {Integer[]} cost
# @return {Integer}
def min_cost_climbing_stairs(cost)
    cost << 0
    n = cost.size
    return cost[0] if n == 1
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, cost[0], cost[1]

    3.upto(n + 1) do |i| 
        dp[i] = cost[i - 1] + [dp[i - 1], dp[i - 2]].min
    end

    dp[n]
end