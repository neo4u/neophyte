# @param {Integer} x
# @return {Integer}
def my_sqrt(x)
    return x if [0, 1].include?(x)
    l, r = 0, x
    puts "l: #{l} | r: #{r} | x: #{x}"

    while l < r
        mid = (l + r) / 2
        if x < mid * mid
            r = mid
        elsif x > mid * mid
            l = mid + 1
        else
            return mid
        end
        puts "mid: #{mid}, l: #{l}, r: #{r}"
    end

    l - 1
end

# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/

# Approach 1: Binary Search
# 1. x < mid * mid means mid is too high, so we search is 1st half l - mid, so make r = mid
# 2. x > mid * mid means mid is too low, so we search 2nd half mid + 1 to r, so make l = mid + 1
# 3. x == mid * mid, also follows the suit with x > mid * mid

# Example: x = 256
# l: 0 | r: 256 | x: 256
# mid: 128
# mid: 64
# mid: 32
# mid: 16 return 16


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(my_sqrt(4), 2)
assert_equal(my_sqrt(256), 16)
assert_equal(my_sqrt(8), 2)
