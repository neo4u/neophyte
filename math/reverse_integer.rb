def reverse( x)
    return x if !x || x.zero?
    sign = x / x.abs # capture the sign by dividing by absolute value
    x *= sign        # Make positive if sign was negative

    rev = 0          # Make a var for storing reverse
    until x.zero?
        pop = x % 10        # pop from back of x
        rev = rev*10 + pop  # fit into back of rev
        x /= 10             # delete the last element
    end

    rev < 1<<31 ? rev*sign : 0 # return 0 if overflow occured
end

# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

# Approach 1: Pop from from back of x and push into back of reverse
# Steps
# 1. Use mod to pop from back of x
# 2. use rev * 10 + pop to add to the end of rev
# 3. div by x to remove the inserted digit

# Time: O(log(x)), log base 10 (x) digits
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(reverse(-123), -321)
assert_equal(reverse(-234342323), -323243432)
assert_equal(reverse(2147483648), 0)
