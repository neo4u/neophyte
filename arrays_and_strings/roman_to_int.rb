# @note Calculate of Romans from range 1 to 3999.
# @param {String} s
# @return {Integer}
def roman_to_int(s)
  prev, val = nil, 0
  romans = { 'I' => 1, 'V' => 5, 'X' => 10, 'L' => 50, 'C' => 100, 'D' => 500, 'M' => 1000 }

  s.chars.reverse.each do |c|
    curr = romans[c]
    if prev && curr >= prev
      val += curr
    elsif prev && curr < prev
      val -= curr
    elsif !prev
      val += curr
    end
    prev = curr
  end

  val
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(roman_to_int('DCXXI'), 621)
assert_equal(roman_to_int('XCVIII'), 98)
assert_equal(roman_to_int('MCMXCVI'), 1996)
