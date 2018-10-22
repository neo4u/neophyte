# @param {Integer} n
# @return {String}
def count_and_say(n)
    nums = ['1']

    while !(n -= 1).zero?
        nums << say(nums.last)
    end

    nums.last
end

def say(num)
    str, prv_c, count = '', '', 0

    num.each_char do |c|
        if prv_c == c || prv_c.empty?
            count += 1 # We're seeing a repeating number (as char) so inc count
        else
            str += count.to_s + prv_c
            count = 1 # because we've seen this number(as char) for the first time
        end
        prv_c = c
    end

    str += count.to_s + prv_c
end

# 38. Count and Say
# https://leetcode.com/problems/count-and-say/

# Time: O(n^2), If you calculate all the string from 1 to n,
#       the total loop num is 1 + 2 + 3 + ... + n = n * (n + 1) / 2
# Space: O(n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(count_and_say(1), '1')
assert_equal(count_and_say(2), '11')
assert_equal(count_and_say(3), '21')
assert_equal(count_and_say(4), '1211')
assert_equal(count_and_say(5), '111221')

