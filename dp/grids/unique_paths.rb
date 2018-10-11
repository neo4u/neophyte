# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)
    dp = Array.new(m) { Array.new(n, 1) }
    1.upto(m - 1) do |i|
        1.upto(n - 1) do |j|
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        end
    end
    
    dp[m - 1][n - 1]
end
