# @param {Integer} n
# @return {Integer}
def climb_stairs(n)
    return 1 if n == 1

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 2

    3.upto(n) do |i| 
        dp[i] = dp[i - 1] + dp[i - 2]
    end

    dp[n]
end
