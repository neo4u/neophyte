# @param {Integer} n
# @return {String}
def count_and_say(n)
  nums = ['1']
  until (n -= 1).zero?
    nums << say(nums.last)
  end

  nums.last
end

def say(num)
  str, prv_c, count = '', '', 0

  num.each_char do |c|
    if prv_c == c || prv_c.empty?
      count += 1
    else
      str += count.to_s + prv_c
      count = 1 # because we've seen this number(char) once
    end
    prv_c = c
  end

  str += count.to_s + prv_c
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(count_and_say(1), '1')
assert_equal(count_and_say(2), '11')
assert_equal(count_and_say(3), '21')
assert_equal(count_and_say(4), '1211')
assert_equal(count_and_say(5), '111221')

# 38. Count and Say