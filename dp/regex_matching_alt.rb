# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m, n = s.length, p.length
    dp = Array.new(m + 1) { Array.new(n + 1, false) }
    dp[0][0] = true

    1.upto(n) do |j|
        dp[0][j] = dp[0][j-2] if p[j - 1] == '*'
    end

    1.upto(m) do |i|
        1.upto(n) do |j|
            dp[i][j] = dp[i - 1][j - 1] if p[j - 1] == s[i - 1] || p[j - 1] == '.'

            if p[j - 1] == '*'
                dp[i][j] = dp[i][j - 2]
                # If s[i] matches p[j-1] only then we can check for a match with s upto i - 1 and j (offset of -1 in indexes)
                dp[i][j] ||= dp[i - 1][j] if p[j - 2] == s[i - 1] || p[j - 2] == '.'
            end
        end
    end

    dp[m][n]
end

# dp
# Time:  O(m * n)
# Space: O(m * n)

# dp[i][j represents whether the substring of s with length i from right can be matched with the substring of p with length j from right.
# Cases
# 1. if s[i] == p[j] dp[i][j] == dp[i - 1][j - 1]
# 2. elsif s[i] != p[j] and p[j] == '.' dp[i][j] == dp[i - 1][j - 1]
# 3. elsif s[i] != p[j] and p[j] == '*'
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
assert_equal(is_match('ab', '.*'), true)
assert_equal(is_match('mississippi', 'mis*is*p*.'), false)
assert_equal(is_match('aab', 'c*a*b'), true)
assert_equal(is_match('aab', 'c*a*b'), true)
assert_equal(is_match('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s'), true)
