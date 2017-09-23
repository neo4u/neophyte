# Assumes a consists of interger values between 0 and k
def counting_sort(a, k)
  # Array a is the input, b is the output, c is temp storage
  c = []
  b = []
  0.upto(k) do |i|
    c[i] = 0
  end

  # c[i] repsents the count of integer i in the input array which is set to 1 in this loop
  0.upto(a.size - 1) do |j|
    c[a[j]] += 1
  end
  p(c)

  # Count number of items less than i
  1.upto(k) do |i|
    c[i] += c[i - 1]
  end
  p(c)

  # (a.size - 1).downto(0) do |j|
  0.upto(a.size - 1) do |j|
    c[a[j]] -= 1
    b[c[a[j]]] = a[j]
  end

  b
end

# a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# k = 9
# p(counting_sort(a, k))
