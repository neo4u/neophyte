# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m, n = s.length, p.length
    dp = Array.new(m + 1) { Array.new(n + 1, false) }

    # Empty string and pattern are a match
    dp[0][0] = true

    # This is to match the * chars of the pattern with empty chars of string
    1.upto(n) do |j|
        dp[0][j] = dp[0][j - 2] if p[j - 1] == '*'
    end

    1.upto(m) do |i|
        1.upto(n) do |j|
            dp[i][j] = dp[i - 1][j - 1] if p[j - 1] == s[i - 1] || p[j - 1] == '.'

            if p[j - 1] == '*'
                # (when j - 1 is at * and i - 1 is z)
                # consider z and aa* dp[i][j] = false because dp[i][j - 2] is compares z and a and that results in false
                # However, consider a and aa* dp[i][j] = true 'cuz we're comparing a with two chars before * which is a hence match
                dp[i][j] = dp[i][j - 2]
                # If s[i] matches p[j-1], only then can we check for a match with s upto i - 1 and j (offset of -1 in indexes)
                dp[i][j] ||= dp[i - 1][j] if s[i - 1] == p[j - 2] || p[j - 2] == '.'
                # consider az and aa* s[i - 1] (z) and p[j - 2j(a) are not a match thus dp[i][j] = false (when j - 1 is at * and i - 1 is z)
                # consider aa and aa* s[i - 1] (a) and p[j - 2](a) are a match thus dp[i][j] = true (when j - 1 is at * and i - 1 is a)
            end
        end
    end

    dp[m][n]
end

# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/

# Approach 1: Recursion

# Approach 2: DP
# Time:  O(m * n)
# Space: O(m * n)

# dp[i][j] represents a match between substrings of length i and j. i.e.; s[0...i - 1] and p[0...j - 1]
# Cases
# 1. if s[i - 1] == p[j - 1] dp[i][j] == dp[i - 1][j - 1]
# 2. elsif s[i - 1] != p[j - 1] and p[j - 1] == '.' then dp[i][j] == dp[i - 1][j - 1]
# 3. elsif s[i-1] != p[j-1] and p[j] == '*'
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
