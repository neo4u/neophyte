# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m, n = s.length, p.length
    dp = Array.new(m + 1) { Array.new(n + 1, false) }
    dp[0][0] = true

    0.upto(n - 1) do |j|
        dp[0][j + 1] = dp[0][j] if p[j] == '*'
    end

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            dp[i + 1][j + 1] = dp[i][j] if p[j] == s[i] || p[j] == '?'
            dp[i + 1][j + 1] = dp[i][j + 1] || dp[i + 1][j] if p[j] == '*'
        end
    end

    dp[m][n]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_match('aa', 'a'), false)
assert_equal(is_match('ab', '*'), true)
assert_equal(is_match('abcd', '*'), true)
assert_equal(is_match('adceb', '*a*b'), true)
assert_equal(is_match('acdcb', 'a*c?b'), false)
assert_equal(is_match('xb', 'xa*'), false)
assert_equal(is_match('xa', 'xa*'), true)
