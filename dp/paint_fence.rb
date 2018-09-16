# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def num_ways(n, k)
    return 0 if n.zero?
    dp = [0] * n
    dp[0], dp[1] = k, k * k

    2.upto(n - 1) do |i|
        dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
    end

    dp[n - 1]
end
