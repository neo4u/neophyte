# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    return word2.size if word1.empty?
    return word1.size if word2.empty?

    m, n = word1.size, word2.size
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }

    1.upto(m) { |i| dp[i][0] = i } # Empty to string of length i will be i insertions
    1.upto(n) { |j| dp[0][j] = j } # String of length j to empty string will be j deletions

    1.upto(m) do |i|
        1.upto(n) do |j|
            if word1[i - 1] == word2[j - 1]
                dp[i][j] = dp[i - 1][j - 1]
            else
                dp[i][j] = [
                    dp[i - 1][j - 1],   # Replace Comparing ab to cd dp[i - 1][j - 1] represents min dist from a to c which require 1 replace if diff
                    dp[i - 1][j],       # Insert Comparing ca to cz dp[i - 1][j] represents min dist from c to ca which require 1 insertion
                    dp[i][j - 1]        # Delete Comparing ca to cz dp[i][j - 1] is cz to c which require 1 deletion
                ].min + 1
            end
        end
    end

    dp[m][n]
end

# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
# https://leetcode.com/problems/edit-distance/description/

# dp[i][j] represent the shortest edit distance between substring word1[0...i - 1] of length i and substring word2[0...j - 1] of length j.
# Then compare the last character of word1[0...i - 1] and word2[0...j - 1]
# Cases:
# if w1[i - 1] == w2[j - 1]
#       then dp[i][j] = dp[i - 1][j - 1] equals edit distance of substrings with 1 char less
# Else
#       We consider minimum of (replace, insert or delete) + 1
#              | dp[i - 1][j - 1],   Replace, Ex. Comparing ab to cd dp[i - 1][j - 1] is a to c which require 1 replace
#       min of | dp[i - 1][j],       Insert, Ex. Comparing ca to cz dp[i - 1][j] is c to ca which require 1 insertion
#              | dp[i][j - 1]        Delete, Ex. Comparing ca to cz dp[i][j - 1] is cz to c which require 1 deletion
#       + 1

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(min_distance('horse', 'ros'), 3)
assert_equal(min_distance('intention', 'execution'), 5)
