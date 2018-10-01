# @param {Integer} n
# @return {Integer}
def climb_stairs(n)
    return 1 if n == 1
    dp = Array.new(n, 0)
    dp[0], dp[1], dp[2] = 1, 2, 3
    
    3.upto(n - 1) do |i|
        dp[i] = dp[i - 1] + dp[i - 2]
    end
    
    dp[n - 1]
end

# dp[i - 1] represents the number of ways to reach the ith step
# our goal is to get dp[n - 1]
# recurrence is:
# dp[i] = dp[i - 1] + dp[i - 2] from 3 to n - 1

# Time: O(n)
# Space: O(n)