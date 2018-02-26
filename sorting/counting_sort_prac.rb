# Assumes a consists of interger values between 0 and k
def counting_sort(a)
  b, c, k = [], [], a.max

  0.upto(k) do |i|
    c[i] = 0
  end

  0.upto(a.size - 1) do |j|
    c[a[j]] += 1
  end

  1.upto(k) do |i|
    c[i] += c[i - 1]
  end

  (a.size - 1).downto(0) do |j|
    c[a[j]] -= 1
    b[c[a[j]]] = a[j]
  end

  b
end

# a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# p(counting_sort(a))
