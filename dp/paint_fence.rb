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

# If ways[i] is the number of ways to paint i posts, then:

# ways[0] = 0 (I think it should be 1, but whatever...)
# ways[1] = k
# ways[2] = k * k
# ways[i>2] = (ways[i-1] + ways[i-2]) * (k - 1)

# The i>2 case is like that because you can use the color for the last post just for the last post or for the two last posts, extending either the i-1 or the i-2 case, and in both cases, you must choose from the k-1 colors that the case you're extending didn't end with.