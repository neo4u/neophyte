# @param {String} num
# @return {Boolean}
def is_strobogrammatic(num)
    strobo_pairs = Set.new([
        ["0", "0"], ["1", "1"],
        ["6", "9"], ["9", "6"],
        ["8", "8"]
    ])
    l, r = 0, num.size - 1

    while l <= r
        # this means that the inverted version of the current number
        # 1. either doesn't exist in strobo pairs map
        # 2. or that if exists doesn't have the matching char at r
        return false if !strobo_pairs.include?([num[l], num[r]])
        l += 1; r -= 1
    end

    true
end


# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

# Time: O(n)
# Space: O(1)

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_strobogrammatic("69"), true)
assert_equal(is_strobogrammatic("88"), true)
assert_equal(is_strobogrammatic("962"), false)
