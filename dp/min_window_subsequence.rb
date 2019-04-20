# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
    m, n = t.size, s.size
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }
    0.upto(n) { |j| dp[0][j] = j + 1 }              # Base Case, empty string is par

    1.upto(m) do |i|
        1.upto(n) do |j|
            if t[i - 1] == s[j - 1]
                dp[i][j] = dp[i - 1][j - 1]
            else
                dp[i][j] = dp[i][j - 1]
            end
        end
    end

    start, len = 0, n + 1
    1.upto(n) do |j|
        if dp[m][j] != 0
            if j - dp[m][j] + 1 < len
                start = dp[m][j] - 1
                len = j - dp[m][j] + 1
            end
        end
    end
    print_matrix(dp)
    puts "start: #{start} | len: #{len}"
    len == n + 1 ? "" : s[start...start + len]
end

def print_matrix(matrix)
    matrix.each do |a|
        puts a.inspect
    end
    puts
end

# 727. Minimum Window Subsequence
# https://leetcode.com/problems/minimum-window-subsequence/


# Approach 1: DP
# Steps:
# dp[i][j] stores the starting index of subsequence T[0, i - 1] in S[0, j - 1].
# 1. Recurrence relation:
#    if T[i - 1] == S[j - 1]
#       dp[i][j] = dp[i - 1][j - 1] (Borrow from diagnoal top left)
#    else
#       dp[i][j] = dp[i][j - 1] 	(Borrow from same row left column)

# 2. Base Case: dp[0][j] = j + 1 for all j from 1 to n
#    Can be interpreted as empty subsequence is always found after my current index
#    at the end of the string.

# 3. End Case: 
# Use indexes in the bottom row to find the subsequence that has min len and appears first

# Possible improvements
# Can be optimized by only storing only last window as that's the only thing needed.

# Example
# S = "abcdebdde", T = "bde"
#   '' a b c d e b d d e
# '' 1 2 3 4 5 6 7 8 9 10
# b  0 0 2 2 2 2 6 6 6 6 
# d  0 0 0 0 2 2 2 6 6 6
# e  0 0 0 0 0 2 2 2 2 6

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 0, 2, 2, 2, 2, 6, 6, 6, 6]
[0, 0, 0, 0, 2, 2, 2, 6, 6, 6]
[0, 0, 0, 0, 0, 2, 2, 2, 2, 6]

# Time: O(mn)
# Space: O(mn)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(min_window("abcdebdde","bde"), "bcde")