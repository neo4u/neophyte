#!/usr/bin/env ruby


# --------------------------------------------------------------------------------
# Class to do word conversion
# --------------------------------------------------------------------------------
class WordConverter
  @words = {
    1 => "one",
    2 => "two",
    3 => "three",
    4 => "four",
    5 => "five",
    6 => "six",
    7 => "seven",
    8 => "eight",
    9 => "nine",
    10 => "ten",
    11 => "eleven",
    12 => "twelve",
    13 => "thirteen",
    14 => "fourteen",
    15 => "fifteen",
    16 => "sixteen",
    17 => "seventeen",
    18 => "eighteen",
    19 => "nineteen",
    20 => "twenty",
    30 => "thirty",
    40 => "fourty",
    50 => "fifty",
    60 => "sixty",
    70 => "seventy",
    80 => "eighty",
    90 => "ninety",
    100 => "hundred",
    1_000 => "thousand",
    1_000_000 => "million",
    1_000_000_000 => "billion",
    1_000_000_000_000 => "trillion"
  }
  @num_in_words = ""
  @sign = ""

  def self.to_words(num)
    if num < 0
      @sign += "minus "
      num = -num
    end

    if num.eql?(0)
      return ""
    elsif num > 0 && num <= 20
      return @sign + ("#{@words[num]} " + to_words(0)).strip
    elsif num > 20 && num <= 100
      return @sign + (num == 100 ? "#{@words[num / 100]} #{@words[num]}" : ("#{@words[(num / 10) * 10]} " + to_words(num % 10)).strip)
    elsif num > 100 && num <= 1000
      return @sign + (num == 1000 ? "#{@words[num / 1000]} #{@words[num]}" : ("#{@words[num / 100]} hundred and " + to_words(num % 100)).chomp(" and "))
    elsif num > 1000 && num <= 1_000_000
      return num == 1_000_000 ? "#{@words[num / 1_000_000]} #{@words[num]}" : "#{to_words(num / 1000)} thousand " + to_words(num % 1000).strip
    elsif num > 1_000_000 && num <= 1_000_000_000
      return num == 1_000_000_000 ? "#{@words[num / 1_000_000_000]} #{@words[num]}" : "#{to_words(num / 1_000_000)} million " + to_words(num % 1_000_000).strip
    elsif num > 1_000_000_000 && num <= 1_000_000_000_000
      return num == 1_000_000_000_000 ? "#{@words[num / 1_000_000_000_000]} #{@words[num]}" : "#{to_words(num / 1_000_000_000)} billion " + to_words(num % 1_000_000_000).strip
    end
  end

  def convert(num)
    WordConverter.to_words(num)
  end
end

converter = WordConverter.new
num = -999_999_500_121
puts "Number in digits: #{num}"
puts "Number in words: #{converter.convert(num)}"
