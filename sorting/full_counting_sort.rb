def counting_sort(a)
  b, c = [], []
  k = nil
  a.each do |hash|
    k = hash.keys.first if k.nil? || k < hash.keys.first
  end

  0.upto(k) do |i|
    c[i] = 0
  end

  # c[i] repsents the count of integer i in the input array which is set to 1 in this loop
  a.each do |hash|
    c[hash.keys.first] += 1
  end

  # Count number of items less than i
  1.upto(k) do |i|
    c[i] += c[i - 1]
  end

  (a.size - 1).downto(0) do |j|
    c[a[j].keys.first] -= 1
    b[c[a[j].keys.first]] = a[j].values.first
  end

  b.join(" ")
end

count = gets.strip.to_i
a = []
(0...count).each_with_index do |_, i|
  k, v = gets.strip.split
  k, v = k.to_i, v.strip
  h = {}
  v = '-' if i >= 0 && i <= count/2 - 1 
  h[k] = v
  a.push(h)
end

p(counting_sort(a))
