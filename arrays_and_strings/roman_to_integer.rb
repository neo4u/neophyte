# @param {String} s
# @return {Integer}
def roman_to_int(s)
  roman = { 'M' => 1000, 'D' => 500, 'C' => 100, 'L' => 50, 'X' => 10, 'V' => 5, 'I' => 1 }
  z = 0
  0.upto(s.size - 2) do |i|
    if roman[s[i].upcase] < roman[s[i + 1].upcase]
      z -= roman[s[i].upcase]
    else
      z += roman[s[i].upcase]
    end
  end

  z + roman[s[-1].upcase]
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(roman_to_int('XVIII'), 18)
assert_equal(roman_to_int('xviii'), 18)
assert_equal(roman_to_int('I'), 1)
assert_equal(roman_to_int('MMD'), 2500)
assert_equal(roman_to_int('IX'), 9)
assert_equal(roman_to_int('X'), 10)
assert_equal(roman_to_int('IIIX'), 11)

# 13. Roman to Integer
