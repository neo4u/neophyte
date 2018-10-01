# @param {String} s
# @param {String} t
# @return {Integer}
def num_distinct(s, t)
    m, n = s.size(), t.size()
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }

    0.upto(m) do |i|
        dp[i][0] = 1
    end

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            if s[i] == t[j]
                dp[i + 1][j + 1] = dp[i][j] +   # number of sequences for s[0...i - 1] and t[0...j-1] one less char in s and t [with s[i] contribution]
                                   dp[i][j + 1] # number of sequences for s[0...i - 1] and t[0...j]   one less char in s only [without s[i] contribution
            else
                dp[i + 1][j + 1] = dp[i][j + 1] # one less char in s only 
            end
        end
    end

    dp[m][n] # notice the reversal of m and n
end

# The idea is the following:

# dp[i+1][j+1] represents the count that S[0..j] (lenght j) contains T[0..i] (length i)
# that many times as distinct subsequences.
# Therefore the result will be dp[T.length()][S.length()]

# From here we can easily fill the whole grid: for each (x, y),
# we check if S[x] == T[y] we add the previous item and the previous item in the previous row, otherwise we copy the previous item in the same row. The reason is simple:
# - if s[i] != t[j], then we have the same number of distinct subsequences as we had without the new character. So we go 1 row above on the same column
# - if s[i] == t[j], then the distinct number of subsequences:
#                       the number we had before (1 row above on the same column)
#                       plus  the distinct number of subsequences we had with less longer S and less longer T.
# An example:
# S: [acdabefbc] and T: [ab]

# S abcde T ade
#   T 0123
#      ade
#     0123
# S  +----+
# 0  |1000|
# 1 a|1100|
# 2 b|11  |
# 3 c|1zy |
# 4 d|1 x |
# 5 e|1...|
# consider dp[4][2] which is comparing s: abcd t: ad marked x
# s[i] is d == t[j] is d
# so we've to add the below two items:
# 1. dp[3][2] s:abc t:ad marked y above. One less item for s
# 2. dp[3][1] s:abc t:a  marked z above. One less item for both s and t

# example:
# S: abcd T:abd and you're comparing c and d chars s[i]!= t[j] so dp[i][j] = dp[i - 1][j]
# which means compare ab abd and copy over their value, because s[i] char is not contributing to the subsequences count
#   T 0123
#    ''abd
# S  +----+
# 0''|1000|
# 1 a|1100|
# 2 b|11 y|
# 3 c|1  x| y is copied over is x position because c doesn't contribute the distinct sequences count
# 4 d|1   |
# let's first calculate A[1][1].
# Because t[0] = 'a' == s[0] = 'a', A[1][1] = A[0][1] + A[0][0] = 1.
# Then, we can calculate A[1][2], Because t[1] = 'b' ≠ s[0] = 'a', A[1][2] = A[0][2] = 0.
# We can fill in A in this way. The final result is shown as follows:
#         ''  a   b
#     A   0   1   2
# ''  0   1   0   0
# a   1   1   1   0
# b   2   1   1   1
# c   3   1   1   1
# a   4   1   2   1
# b   5   1   2   3

# lets say you're comparing abc and ab and we're at i = 2 and j = 1 s[i] is c and t[j] is b s[i] != t[j],
# so we consider the same number as ab and ab that dp[i - 1][j]

# lets say you're comparing abc and bc and we're at i = 2 and j = 1 now s[i] == s[j]
# So we consider adding the subsequences of ab and b plus ab and bc


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(num_distinct("rabbbit", "rabbit"), 3)
assert_equal(num_distinct("babgbag", "bag"), 5)

