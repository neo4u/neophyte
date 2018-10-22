ROMANS = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'].reverse
VALUES = [  1,    4,   5,    9,  10,   40,  50,   90, 100,  400, 500,  900, 1000].reverse

def int_to_roman(num)
    res, i = "", 0

    until num.zero?
        puts i
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
