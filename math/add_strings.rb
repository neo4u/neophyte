# Using pop, feels like cheating cuz classic array ADT doesn't have a pop operation
# @param {String} num1
# @param {String} num2
# @return {String}
def add_strings(num1, num2)
    carry, result, num1, num2 = 0, '', num1.chars, num2.chars

    while !num1.empty? || !num2.empty?
        d1 = !num1.empty? ? num1.pop.to_i : 0
        d2 = !num2.empty? ? num2.pop.to_i : 0
        
        carry, d = (d1 + d2 + carry).divmod(10)
        result = d.to_s + result
    end

    carry == 0 ? result : carry.to_s + result
end

# 415. Add Strings
# https://leetcode.com/problems/add-strings/

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(add_strings('21', '12'), 33)
assert_equal(add_strings('15', '1'), 16)
assert_equal(add_strings('21', '12'), 33)

