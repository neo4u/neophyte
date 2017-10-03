# @param {String} s
# @return {Boolean}
def is_valid(s)
  stack = []
  s.each_char do |c|
    if c == '('
      stack.push(')')
    elsif c == '{'
      stack.push('}')
    elsif c == '['
      stack.push(']')
    elsif stack.empty? || c != stack.pop
      return false
    end
  end
  stack.empty?
end

# for char in s:
#   if char in dict.values():
#       stack.append(char)
#   elif char in dict.keys():
#       if stack == [] or dict[char] != stack.pop():
#           return False
#   else:
#       return False
# return stack == []

p is_valid("()")