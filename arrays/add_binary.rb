def add_binary(a, b)
    i, j = a.size - 1, b.size - 1
    result, carry = '', 0
    
    while i >= 0 || j >= 0
        d1 = i >= 0 ? a[i].to_i : 0
        d2 = j >= 0 ? b[j].to_i : 0

        sum = d1 + d2 + carry
        if sum == 1 || sum == 0
            result = sum.to_s + result
            carry = 0
        elsif sum == 2
            result = '0' + result
            carry = 1
        elsif sum == 3
            result = '1' + result
            carry = 1
        end
        i -= 1; j -= 1
    end

    carry == 1 ? "1" + result : result
end

# Descriptive manual addition
# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    a, b = a.chars, b.chars
    result, carry = '', 0

    while !a.empty? || !b.empty?
        d1 = !a.empty? ? a.pop.to_i : 0
        d2 = !b.empty? ? b.pop.to_i : 0

        sum = d1 + d2 + carry
        if sum == 1 || sum == 0
            carry = 0
            result = sum.to_s + result
        elsif sum == 2
            result = '0' + result
            carry = 1
        elsif sum == 3
            result = '1' + result
            carry = 1
        end
    end

    result = carry.to_s + result if carry == 1
    result
end

def add_binary(a, b)
    i, j = a.size - 1, b.size - 1
    result, carry = '', 0
    
    while i >= 0 || j >= 0
        d1 = i >= 0 ? a[i].to_i : 0
        d2 = j >= 0 ? b[j].to_i : 0

        sum = d1 + d2 + carry
        if sum == 1 || sum == 0
            result = sum.to_s + result
            carry = 0
        elsif sum == 2
            result = '0' + result
            carry = 1
        elsif sum == 3
            result = '1' + result
            carry = 1
        end
        i -= 1; j -= 1
    end

    carry == 1 ? "1" + result : result
end

# Using % 2 on the sum
# @param {String} a
# @param {String} b
# @return {String}
def add_binary_alt(a, b)
    res, sum = "", 0
    i, j = a.size - 1, b.size - 1

    while i >= 0 || j >= 0 || sum == 1
        sum += a[i] == '0' ? 0 : 1  if i >= 0
        sum += b[j] == '0' ? 0 : 1  if j >= 0
        res = (sum % 2).to_s + res
        sum /= 2 # carry only if sum is 2 (in case of carry 1 + 1 + 1), 1/2 and 0/2 become 0, hence no carry

        i -= 1
        j -= 1
    end

    res
end

# Using ruby eval
def add_binary(a, b)
    (eval('0b' + a) + eval('0b' + b)).to_s(2)
end


# 67. Add Binary
# https://leetcode.com/problems/add-binary/

# n is max of size of a and b
# Time: O(n)
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

# assert_equal(add_binary('11', '1'), '100')
# assert_equal(add_binary('1010', '1011'), '10101')

# assert_equal(add_binary_alt('11', '1'), '100')
# assert_equal(add_binary_alt('1010', '1011'), '10101')


assert_equal(add_binary_ptr('11', '1'), '100')
assert_equal(add_binary_ptr('1010', '1011'), '10101')
