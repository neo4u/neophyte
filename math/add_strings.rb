# @param {String} num1
# @param {String} num2
# @return {String}
def add_strings(num1, num2)
    i, j = num1.size - 1, num2.size - 1
    result, carry = '', 0
    
    while i >= 0 || j >= 0
        d1 = i >= 0 ? num1[i].to_i : 0
        d2 = j >= 0 ? num2[j].to_i : 0
        
        carry, d = (d1 + d2 + carry).divmod(10)
        result = d.to_s + result
        i -= 1; j -= 1
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

