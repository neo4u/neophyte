def counting_sort(a, b, k)
  c = []
  0.upto(k) do |i|
    c[i] = 0
  end

  0.upto(a.size - 1) do |j|
    c[a[j]] += 1
  end

  1.upto(a.size - 1) do |i|
    c[i] += c[i - 1]
  end

  (a.size - 1).downto(0) do |j|
    c[a[j]] -= 1
    b[c[a[j]]] = a[j]
  end

  b
end