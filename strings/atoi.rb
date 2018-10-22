# @param {String} str
# @return {Integer}
def my_atoi(str)
    return 0 if str.empty?
    ls = str.strip().chars
    sign = ls[0] == '-' ? -1 : 1
    ls.shift if ['-','+'].include?(ls[0])
    ret, i = 0, 0

    while i < ls.size && digit?(ls[i])  # Exit as soon as we find a non-digit
        ret = ret * 10 + ls[i].ord - '0'.ord
        i += 1
    end

    [-2**31, [sign * ret, 2**31 - 1].min].max
end

def digit?(c)
    c.between?('0', '9')
end

# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/

# Approach 1
# 1. Strip input and get chars in an array
# 2. capture sign and delete the sign from array start
# 3. process each char that is a digit
# 4. and add to integer result (ret * 10 + str digit.ord)
# 5. as soon as we encounter a non-digit exit and return the result
# 6. Ensure there is no overflow at the return of result. Has to be 32 bit integer.

# Approach 2: Refer java file with same name
# DFA
# 1. keep track of all the valid states
# 2. Define valid transitions
# 3. as soon as we hit an invalid state
# 4. return the signed current integer value

# Time: O(n)
# Space: O(n), to store ls array

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(my_atoi("-1 2 3 4"), -1234)
assert_equal(my_atoi("+-2"), 0)
assert_equal(my_atoi("-1"), -1)
assert_equal(my_atoi("-0012a42"), -12)
assert_equal(my_atoi("   +0 123"), 0)
assert_equal(my_atoi("123  456"), 123)
assert_equal(my_atoi("   - 321"), 0)
assert_equal(my_atoi("    010"), 10)

