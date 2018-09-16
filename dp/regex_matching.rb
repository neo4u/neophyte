# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m, n = s.size, p.size
    dp = Array.new(m + 1) { Array.new(n + 1, false) }
    dp[0][0] = true

    0.upto(n - 1) do |i|
        dp[0][i + 1] = dp[0][i - 1] if p[i] == '*'
    end

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            dp[i + 1][j + 1] = dp[i][j] if p[j] == '.' || p[j] == s[i]

            if p[j] == '*'
                dp[i + 1][j + 1] = dp[i][j + 1] || dp[i + 1][j] if p[j] == '*'

                # dp[i + 1][j + 1] = dp[i + 1][j - 1]
                # dp[i + 1][j + 1] ||= dp[i][j + 1] if p[j - 1] == s[i] || p[j - 1] == '.'
            end
        end
    end

    dp[m][n]
end

# dp
# Time:  O(m * n)
# Space: O(m * n)

# dp[i + 1][j + 1] is the match result of s[0, i] and p[0, j];
# Cases
# 1. if s[i] == p[j] || p[j] == '.' then dp[i + 1][j + 1] == dp[i][j]
# 3. if p[j] == '*'
#     3.a. Could be the case the * could be interpreted as 0 repititions
#         dp[i][j] = dp[i][j - 2]        ex. s: c and p: ca* We consider the match c which is 2 chars before the *
#     3.b. if s[i] == p[j-1] or p[j - 1] == '.':
#         dp[i][j] = dp[i-1][j]   // in this case, a* counts as multiple a
#      or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_match('aaa', 'ab*ac*a'), true)
assert_equal(is_match('abbbbccc', 'a*ab*bbbbc*'), true)
assert_equal(is_match('aa', 'a'), false)
assert_equal(is_match('aa', 'a*'), true)
assert_equal(is_match('ab', '*'), true)
assert_equal(is_match('mississippi', 'mis*is*p*.'), false)
assert_equal(is_match('aab', 'c*a*b'), true)
assert_equal(is_match('aab', 'c*a*b'), true)
assert_equal(is_match('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'), true)
