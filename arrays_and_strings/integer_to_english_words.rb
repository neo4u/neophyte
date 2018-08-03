# @param {Integer} num
# @return {String}
def number_to_words(num)
  num.eql?(0) ? "Zero" : in_words(num)
end

def in_words(num)
  words = {
    1 => "One", 2 => "Two", 3 => "Three", 4 => "Four", 5 => "Five",
    6 => "Six", 7 => "Seven", 8 => "Eight", 9 => "Nine",
    10 => "Ten", 11 => "Eleven", 12 => "Twelve", 13 => "Thirteen",
    14 => "Fourteen",15 => "Fifteen", 16 => "Sixteen",
    17 => "Seventeen", 18 => "Eighteen", 19 => "Nineteen",
    20 => "Twenty", 30 => "Thirty", 40 => "Forty", 50 => "Fifty",
    60 => "Sixty", 70 => "Seventy", 80 => "Eighty", 90 => "Ninety"
  }

  if num < 20
    return words[num]
  elsif num < 100
    return "#{words[num / 10 * 10]} #{in_words(num % 10)}".strip
  elsif num < 1000
    return "#{words[num / 100]} Hundred #{in_words(num % 100)}".strip
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

assert_equal(number_to_words(123), 'One Hundred Twenty Three')
