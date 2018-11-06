# @param {Integer} n
# @return {String[]}
def find_strobogrammatic(n)
    odd_mid_candidates = ['0', '1', '8']
    even_mid_candidates = ['11', '69', '88', '96', '00']

    if n == 1
        return odd_mid_candidates
    elsif n == 2
        return even_mid_candidates[0...-1]
    elsif n % 2 == 1 # Odd case
        outer, inner = find_strobogrammatic(n - 1), odd_mid_candidates
    else
        outer, inner = find_strobogrammatic(n - 2), even_mid_candidates
    end

    mid = (n - 1) / 2
    result = []
    outer.each do |o|
        inner.each do |i|
            result.push(o[0, mid] + i + o[mid, o.size])
        end
    end

    result
end


# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/

# Approach 1:

# NOTE: 00 is not part of n = 2 result because it's not even a number.
#       (Or rather, not the decimal representation of a number.)

# Insert from 1 or 2 solution middle of (n - 1)th or (n - 2)th solution respectively
# n == 1: [0, 1, 8]
# n == 2: [11, 88, 69, 96]
# How about n == 3
# => it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2
# n == 4?
# => it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2
# n == 5?
# => it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4
# the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(find_strobogrammatic(1), ["0","1","8"])
assert_equal(find_strobogrammatic(2), ["11","69","88","96"])
assert_equal(find_strobogrammatic(3), ["101","111","181","609","619","689","808","818","888","906","916","986"])
assert_equal(find_strobogrammatic(4), ["1111", "1691", "1881", "1961", "1001", "6119", "6699", "6889", "6969", "6009", "8118", "8698", "8888", "8968", "8008", "9116", "9696", "9886","9966", "9006"])


