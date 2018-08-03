
def int_to_roman(num)
  romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'].reverse
  values = [  1,    4,   5,    9,  10,   40,  50,   90, 100,  400, 500,  900, 1000].reverse
  res, i = "", 0

  until num.zero?
    # This is to multiply the number of Xs or Cs or Ms.
    res += (romans[i] * (num / values[i]))
    num %= values[i]
    i += 1
  end

  res
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(int_to_roman(621), 'DCXXI')
assert_equal(int_to_roman(98), 'XCVIII')
assert_equal(int_to_roman(448), 'CDXLVIII')
assert_equal(int_to_roman(1996), 'MCMXCVI')
assert_equal(int_to_roman(3999), 'MMMCMXCIX')
assert_equal(int_to_roman(400), 'CD')

# 12. Integer to Roman
