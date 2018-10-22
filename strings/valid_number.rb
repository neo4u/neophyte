# @param {String} s
# @return {Boolean}
def is_number(s)
    s =~ /\A\s*
        (?:[+-]?)             (?# 1: sign)
        (?:\d+\.?|\d*\.\d+)   (?# 2: significand)
        (?:[eE][+-]?\d+)?     (?# 3: exponent)
    \s*\z/x ? true : false
end

# DFA to regex
# https://www.youtube.com/watch?v=SmT1DXLl3f4 
# https://www.geeksforgeeks.org/theory-computation-generating-regular-expression-finite-automata/

# Regex to DFA
# https://www.geeksforgeeks.org/designing-finite-automata-from-regular-expression/

# 65. Valid Number
# https://leetcode.com/problems/valid-number/

# Time: O(n), Iterate the string once and check for matches
# Space: O(1), Finite and constant number of states

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(is_number("0"), true)
assert_equal(is_number(" 0.1 "), true)
assert_equal(is_number("abc"), false)
assert_equal(is_number("1 a"), false)
assert_equal(is_number("2e10"), true)
