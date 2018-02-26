# @param {String} str
# @return {Integer}
def my_atoi(str)
  int, sign, digit_started, prev = 0, "", false, ""
  str.each_char do |char|
    if char.between?('0', '9')
      int = int * 10 + char.to_i
      digit_started = true
      prev = char
    elsif /\s/.match(char)
      break if [' ', '0'].include?(prev) && (digit_started || !sign.empty?)
      prev = char
    elsif char.between?("a", "z")
      break
    else
      sign += char
    end
  end

  if sign.start_with?("-+", "+-", "++", "--")
    int = 0
  elsif sign.start_with?("-")
    int = -int
  end

  [-2**31, [int, 2**31 - 1].min].max
end

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
# --------------------------------------------------------------------------------
# There are too many input types that could be malformed that need to be handled
# so its not hard but you just need to be exhaustive. Not sure why this code works :(
# --------------------------------------------------------------------------------
# 8. String to Integer (atoi)
# --------------------------------------------------------------------------------
