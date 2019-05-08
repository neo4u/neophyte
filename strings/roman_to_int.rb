# @param {String} s
# @return {Integer}
def roman_to_int(s)
    prev, val = 0, 0
    romans = { 'I' => 1, 'V' => 5, 'X' => 10, 'L' => 50, 'C' => 100, 'D' => 500, 'M' => 1000 }

    s.chars.reverse_each do |c|
        curr = romans[c]
        curr >= prev ? val += curr : val -= curr
        prev = curr
    end

    val
end

# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(roman_to_int('DCXXI'), 621)
assert_equal(roman_to_int('XCVIII'), 98)
assert_equal(roman_to_int('MCMXCVI'), 1996)
