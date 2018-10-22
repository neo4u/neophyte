# Descriptive manual addition
# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    a, b = a.chars, b.chars
    result, carry = [], 0

    while !a.empty? || !b.empty?
        n1 = n2 = 0
        n1 = a.pop.to_i if !a.empty?
        n2 = b.pop.to_i if !b.empty?

        tmp = n1 + n2 + carry
        carry = 0
        if tmp == 1 || tmp == 0
            result.push(tmp)
        elsif tmp == 2
            result.push(0)
            carry += 1
        else
            result.push(1)
            carry += 1
        end
    end

    result.push(carry) if carry == 1
    result.join('').reverse
end


# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    res, sum = "", 0
    i, j = a.size - 1,  b.size - 1
  
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

assert_equal(add_binary('11', '1'), '100')
assert_equal(add_binary('1010', '1011'), '10101')
