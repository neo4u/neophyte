#!/bin/ruby

def common_child(s1, s2)
  n, m = s1.size, s2.size
  lcs = Array.new(n + 1) { Array.new(m + 1, 0) }

  s1.each_char.with_index do |a, i|
    s2.each_char.with_index do |b, j|
      lcs[i][j] = if a == b
                    lcs[i - 1][j - 1] + 1
                  else
                    [lcs[i][j - 1], lcs[i - 1][j]].max
                  end
    end
  end

  lcs[n - 1][m - 1]
end

s1 = gets.strip
s2 = gets.strip
result = common_child(s1, s2)
puts result
