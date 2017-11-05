# @param {String} str
# @return {Integer}
def my_atoi(str)
  digits = str.chars.select { |c| c.ord.between?('0'.ord, '9'.ord) }
  int = 0
  until digits.empty?
    digit = digits.shift
    next if digit.empty?
    int = int * 10 + digit.to_i
  end

  str.start_with?("-") ? -int : int
end

puts my_atoi("-1 2 3 4")
puts my_atoi("+-2") # Should give 0?? WTF why? atoi is crazy

# THere are too many input types that could be malformed that need to be handled
# so its not hard but you just need to be exhaustive