# Approach 1: Top-Down Approach
def is_match(s, p)
    solve(s, p, 0, 0, Array.new(s.size + 1) { Array.new(p.size + 1, nil) })
end

def solve(s, p, i, j, dp)
    return dp[i][j] if dp[i][j] != nil
    if j == p.size
        dp[i][j] = i == s.size
        return dp[i][j]
    end

    base = i < s.size && (p[j] == '.' || s[i] == p[j])
    if j + 1 < p.size && p[j + 1] == '*'
        dp[i][j] = solve(s, p, i, j + 2, dp) || base && solve(s, p, i + 1, j, dp)
    else
        dp[i][j] = base && solve(s, p, i + 1, j + 1, dp)
    end

    dp[i][j]
end

def is_match(s, p) # question 10 regular expression match
    dp(s, p, 0, 0, {})
end

def dp(s, p, i, j, memo)
    return memo[[i, j]] if memo.key?([i, j]) # not explored before
    if j == p.size
        ans = i == s.size
    else
        first_match = i < s.size && [s[i], '.'].include?(p[j])
        ans = if j + 1 < p.size && p[j + 1] == '*'
            dp(s, p, i, j + 2, memo) || first_match && dp(s, p, i + 1, j, memo)
        else
            first_match && dp(s, p, i + 1, j + 1, memo)
        end
    end
    memo[[i, j]] = ans
end



# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m, n = s.length, p.length
    dp = Array.new(m + 1) { Array.new(n + 1, false) }

    # Empty string and pattern are a match
    dp[0][0] = true

    # This is to match the * chars of the pattern with empty chars of string
    # Example 1:   | Example 2:
    #    '' a . *  |   '' . * . *
    # '' T  F F F  | '' T F T F T
    #              | This loop is to fill the top row like in the examples above, helps for examples like
    #              | s: '' p: '.*.*', s: 'a' p: '.*a.*'
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

# Approach 1: Recursion Top-Down Approach
# Time:  O(m * n)
# Space: O(m * n)

# Approach 2: DP
# Time:  O(m * n)
# Space: O(m * n)


# Difference from wildcard is that * is associated with preceding char
# ? and . are the same thing
# .* means 0 or more repititions of any char. "" with ".*" is a match

# dp[i][j] represents a match between substrings of length i and j. i.e.; s[0...i - 1] and p[0...j - 1]
# Cases
# 0. Base case: dp[0][0] == true, Empty s and p are considered a match
# 1. if s[i - 1] == p[j - 1] dp[i][j] == dp[i - 1][j - 1]
# 2. elsif s[i - 1] != p[j - 1] and p[j - 1] == '.' then dp[i][j] == dp[i - 1][j - 1] ; Take value from left diagonally top element
# 3. elsif s[i-1] != p[j-1] and p[j] == '*'
#     3.a. Could be the case the * could be interpreted as 0 repititions as part of char* pattern
#          dp[i][j] = dp[i][j - 2]        ex. s: c and p: ca* We consider the match c which is 2 chars before the *
#          
#     3.b. if s[i] == p[j-1] or p[j - 1] == '.':
#         dp[i][j] = dp[i-1][j]   // in this case, a* counts as multiple a; Take value from row above, same column
#                                  // 1 or more repititions as part of char * pattern
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
assert_equal(is_match('a', '.*a.*'), true)
