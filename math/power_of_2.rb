# @param {Integer} n
# @return {Boolean}
def is_power_of_two(n)
    return false if n <= 0
    n /= 2 while n % 2 == 0

    n == 1 # After dividing by two the least number it can reach before % 2 becomes non-zero is 1
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_power_of_two(25), false)
assert_equal(is_power_of_two(5), false)
assert_equal(is_power_of_two(44), false)
assert_equal(is_power_of_two(4), true)

# Complexity Analysis
# Time complexity: O(logb(n)). In our case that is O(log3n). The number of divisions is given by that logarithm.
# Space complexity: O(1). We are not using any additional memory.