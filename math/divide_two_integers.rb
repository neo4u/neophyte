# @param {Integer} dividend
# @param {Integer} divisor
# @return {Integer}
def divide(dividend, divisor)
    # Calculate sign of divisor i.e., sign will be negative
    # only iff either one of them is -ve else it will be +ve. If do a XOR
    sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1
    dividend, divisor, quotient = dividend.abs, divisor.abs, 0

    while dividend >= divisor
        puts 'outer'
        temp, i = divisor, 1

        while dividend >= temp
            puts 'inner'
            puts "dividend: #{dividend} | divisor: #{divisor} | quotient: #{quotient} | temp: #{temp} | i: #{i}"
            dividend -= temp
            quotient += i

            i <<= 1     # same as i *= 2
            temp <<= 1  # same as temp *= 2
        end
    end
    # Max of least and answer and min of max 32 int and answer,
    # as our solution is bounded by min_int and max_int
    [[-2**31, sign * quotient].max, 2**31-1].min
end

# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

# Binary search like bit manipulation solution
# https://www.sigmainfy.com/blog/leetcode-divide-two-integers.html

# Efficient Approach: Use bit manipulation in order to find the quotient.

# 1. Handling sign
# First, we need to check whether the end result is positive or negative.
# Two cases will lead to negative case which is when dividend and divisor has different signs.

# 2. Handling overflow:
# You know, there are so many corner cases which will lead to overflow.
# So it is better to convert them to long first, and convert it back to integer when returning the value.

# 3. Using subtracting and bit-shifting (or * 2) to do the division
# We know that division is actually the backward of multiplication,
# for example , 20 / 5 = 4 can be seen as 4 * 5 = 20.

# We find the multiplication.
# We set tmp as divisor (5) and set count to 1.
# As long as the tmp is <= dividend (20),
# we left shift << which is same as multiply 2 but without using multiplication.

# Consider 10/2
# We keep doing dividend -= temp
# dividend = 10 - 2, q = 0 + 1 = 1
# dividend = 8 - 4, q = 2 + 1 = 3
# temp = 8 and dividend = 4 at this point hence we need to reset temp to divisor = 2
# dividend = 4 - 2, q = 3 + 1 = 4
# at this point temp = 4, dividend = 2 hence we reset temp = 2
# dividend = 2 - 2, q = 4 + 1 = 5
# our loop breaks here as divided = 0 and divident >= divisor fails

# See demo prints for 10/3
# outer
# inner
# dividend: 10 | divisor: 2 | quotient: 0 | temp: 2 | i: 1
# inner
# dividend: 8 | divisor: 2 | quotient: 1 | temp: 4 | i: 2
# outer
# inner
# dividend: 4 | divisor: 2 | quotient: 3 | temp: 2 | i: 1
# outer
# inner
# dividend: 2 | divisor: 2 | quotient: 4 | temp: 2 | i: 1

# Time: O(1)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(divide(10, 2), 5)
assert_equal(divide(20, 6), 3)
assert_equal(divide(7, -3), -2)

