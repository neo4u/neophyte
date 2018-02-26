# @param {Integer} num
# @return {String}
def number_to_words(num)
  num.eql?(0) ? "Zero" : in_words(num)
end

def in_words(num)
  return "" if num.eql?(0)

  words = {
    1 => "One", 2 => "Two", 3 => "Three", 4 => "Four", 5 => "Five", 6 => "Six", 7 => "Seven", 8 => "Eight", 9 => "Nine", 10 => "Ten",
    11 => "Eleven", 12 => "Twelve", 13 => "Thirteen", 14 => "Fourteen", 15 => "Fifteen", 16 => "Sixteen", 17 => "Seventeen", 18 => "Eighteen", 19 => "Nineteen",
    20 => "Twenty", 30 => "Thirty", 40 => "Forty", 50 => "Fifty", 60 => "Sixty", 70 => "Seventy", 80 => "Eighty", 90 => "Ninety"
  }

  if num < 20
    return words[num].to_s
  elsif num < 100
    return [words[(num / 10) * 10], in_words(num % 10)].join(' ').strip
  elsif num < 1000
    return ["#{words[num / 100]} Hundred", in_words(num % 100)].join(' ').strip
  elsif num < 1_000_000
    return "#{in_words(num / 1000)} Thousand #{in_words(num % 1000)}".strip
  elsif num < 1_000_000_000
    return "#{in_words(num / 1_000_000)} Million #{in_words(num % 1_000_000)}".strip
  elsif num < 1_000_000_000_000
    return "#{in_words(num / 1_000_000_000)} Billion #{in_words(num % 1_000_000_000)}".strip
  end
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(number_to_words(1), 'One')
assert_equal(number_to_words(0), 'Zero')
assert_equal(number_to_words(20), 'Twenty')
assert_equal(number_to_words(25), 'Twenty Five')
assert_equal(number_to_words(99), 'Ninety Nine')
assert_equal(number_to_words(100), 'One Hundred')
assert_equal(number_to_words(123), 'One Hundred Twenty Three')
assert_equal(number_to_words(200), 'Two Hundred')
assert_equal(number_to_words(1000), 'One Thousand')
assert_equal(number_to_words(1234), 'One Thousand Two Hundred Thirty Four')
assert_equal(number_to_words(1996), 'One Thousand Nine Hundred Ninety Six')
assert_equal(number_to_words(2000), 'Two Thousand')
assert_equal(number_to_words(999_001), 'Nine Hundred Ninety Nine Thousand One')
assert_equal(number_to_words(99_000_001), 'Ninety Nine Million One')
assert_equal(number_to_words(1_000_000_000), 'One Billion')
assert_equal(number_to_words(989_000_000_001), 'Nine Hundred Eighty Nine Billion One')
