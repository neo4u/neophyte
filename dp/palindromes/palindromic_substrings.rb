# @param {String} s
# @return {Integer}
def count_substrings(s)
    n = s.length
    dp = Array.new(n) { Array.new(n, false) }
    count = 0

    0.upto(n - 1) do |i|
        dp[i][i] = true
        count += 1
    end

    0.upto(n - 2) do |i|
        next if s[i] != s[i + 1]
        dp[i][i + 1] = true
        count += 1
    end
    
    3.upto(n) do |k|
        0.upto(n - k) do |i|
            # Considering strings of length 3 to n
            j = i + k - 1
            if dp[i + 1][j - 1] && s[i] == s[j]
                dp[i][j] = true
                count += 1
            end
        end
    end

    count
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(count_substrings('aaa'), 6)
assert_equal(count_substrings('aaaaa'), 15)
