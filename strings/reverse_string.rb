# @param {String} s
# @return {String}
def reverse_string(s)
    n = s.size
    0.upto((n - 1) / 2) do |i| # (n - 1) / 2 gives the index middle for odd and before middle for even
        s[i], s[-i - 1] = s[-i - 1], s[i]
    end

    s
end

# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(reverse_string("reverse"), "esrever")
assert_equal(reverse_string("abcd"), "dcba")
assert_equal(reverse_string("cdc"), "cdc")
