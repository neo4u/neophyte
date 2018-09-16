# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    return word2.size if word1.empty?
    return word1.size if word2.empty?

    m, n = word1.size, word2.size
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }

    1.upto(m) { |i| dp[i][0] = i }
    1.upto(n) { |j| dp[0][j] = j }

    1.upto(m) do |i|
        1.upto(n) do |j|
            if word1[i - 1] == word2[j - 1]
                dp[i][j] = dp[i - 1][j - 1]
            else
                dp[i][j] = [
                    dp[i - 1][j - 1],   # Replace
                    dp[i - 1][j],       # Delete
                    dp[i][j - 1]        # Insert
                ].min + 1
            end
        end
    end

    dp[m][n]
end

# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
# https://leetcode.com/problems/edit-distance/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(min_distance('horse', 'ros'), 3)
assert_equal(min_distance('intention', 'execution'), 5)
