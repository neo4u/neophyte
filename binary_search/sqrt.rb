# @param {Integer} x
# @return {Integer}
# def my_sqrt(x)
#     return x if [0, 1].include?(x)
#     l, r = 0, x
#     puts "l: #{l} | r: #{r} | x: #{x}"

#     while l <= r
#         mid = (l + r) / 2
#         mid_sq = mid * mid
#         mid_plus_1_sq = (mid + 1) * (mid + 1)
#         return mid if x.between?(mid_sq, mid_plus_1_sq - 1)
#         x < mid_sq ? r = mid - 1 : l = mid + 1
#         puts "mid: #{mid} | l: #{l} | r: #{r}"
#     end
# end

def my_sqrt(x)
    return x if [0, 1].include?(x)
    l, r = 0, x

    while l < r
        mid = (l + r) / 2
        mid_sq = mid * mid
        x < mid_sq ? r = mid : l = mid + 1
    end

    l - 1 # to get the floor
end



def my_sqrt(x)
    return x if [0, 1].include?(x)
    l, r = 0, x

    while l < r
        mid = (l + r) / 2
        mid_sq = mid * mid
        return mid if mid_sq == x
        x < mid_sq ? r = mid : l = mid + 1
    end

    l - 1 # to get the floor
end

# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/

# Approach 1: Binary Search
# 1. x < mid * mid means mid is too high, so we search is 1st half l to mid, so make r = mid
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



# 8 

# 0   4   8
# l   m   r

# 0  2  4
# l  m  r

# 3   4
# l   r
# m

# 3
# l
# r
# m

# l - 1 == 2

# 16

# 0    8    16
# l    m    r

# 0  4  8
# l  m  r

