ROMANS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
VALUES = [1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,  1]

def int_to_roman(num)
    res, i = "", 0

    while num != 0
        res += (ROMANS[i] * (num / VALUES[i])) # Gives number of romans[i] in num
        num %= VALUES[i]
        i += 1
    end

    res
end

# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

# Approach
# 1. Using string build in. For romans and values 1000 to 1,
#    keep counting how many romans are found in num and append those many romans to result
# 2. Do a mod of that roman value to remove that order of the number and continue to smaller value
# 3. Increment i to iterate through the roman and int values

# Time: O(1), max till 12
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(int_to_roman(621), 'DCXXI')
assert_equal(int_to_roman(98), 'XCVIII')
assert_equal(int_to_roman(448), 'CDXLVIII')
assert_equal(int_to_roman(1996), 'MCMXCVI')
assert_equal(int_to_roman(3999), 'MMMCMXCIX')
assert_equal(int_to_roman(399), 'CCCXCIX')
assert_equal(int_to_roman(400), 'CD')
