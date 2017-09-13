#!/bin/ruby

def richie_rich(str, k)
  s = str.dup
  size = s.size
  odd = true if size.odd?
  loop_count = size / 2
  return '9' if size == 1 && k > 0
  changes = 0

  # Count minimum no. of changes needed to make it a palindrome
  (0...loop_count).each do |i|
    changes += 1 if s[i] != s[-i - 1]
  end

  (0...loop_count).each do |i|
    break if k.zero?
    next if s[i].eql?('9') && s[-i - 1].eql?('9')

    if k >= 2 && k - changes >= 2 && (s[i] != '9' && s[-i - 1] != '9') && s[i] == s[-i - 1]
      s[i] = s[-i - 1] = '9'
      k -= 2
    elsif k >= 2 && k - changes >= 1 && (s[i] != '9' && s[-i - 1] != '9') && s[i] != s[-i - 1]
      s[i] = s[-i - 1] = '9'
      k -= 2
      changes -= 1
    elsif k >= 1 && k - changes >= 1 && (s[i] == '9' || s[-i - 1] == '9')
      s[i] = s[-i - 1] = '9'
      k -= 1
      changes -= 1
    elsif k >= 1 && s[i] == s[-i - 1]
      next
    elsif k >= 1 && s[-i - 1] < s[i]
      s[-i - 1] = s[i]
      k -= 1
      changes -= 1
    elsif k >= 1 && s[i] < s[-i - 1]
      s[i] = s[-i - 1]
      k -= 1
      changes -= 1
    end
  end
  s[loop_count] = '9' if odd && k > 0
  return -1 if s != s.reverse

  s
end

_, k = gets.split.map(&:to_i)
s = gets.strip
result = richie_rich(s, k)
puts result
