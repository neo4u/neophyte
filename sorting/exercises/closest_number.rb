def closest_numbers(a)
  min_dist = Float::INFINITY
  min_dist_pairs = []

  a.each_cons(2) { |x, y| min_dist = (x - y).abs if (x - y).abs < min_dist }
  a.each_cons(2) { |x, y| min_dist_pairs.push(x, y) if (x - y).abs == min_dist }

  min_dist_pairs.join(" ")
end

count = gets.strip.to_i
a = gets.split.map(&:to_i).sort
puts closest_numbers(a)

