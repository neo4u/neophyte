def get_substrings(s)
  counter = 0
  res, n = "", s.size
  dp = Array.new(n) { Array.new(n, false) }
	0.upto(n - 1) do |i|
		0.upto(i) do |j|
			puts "#{j}, #{i}"
      puts "#{counter += 1}: #{s[j..i]}"
		end
		puts "\n"
  end
end

get_substrings("silence")