def get_substrings(s)
  counter = 0
  res, n = "", s.size
  dp = Array.new(n) { Array.new(n, false) }
  0.upto(n - 1) do |i|
    i.upto(n - 1) do |j|
      puts "#{counter += 1}: #{s[i..j]}"
    end
  end
end

get_substrings("silence")