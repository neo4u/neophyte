# Steps

# split
# sort
# merge

def merge(a, p, q, r)
  n1, n2 = q - p + 1, r - q
  left, right = [], []

  0.upto(n1 - 1) do |i|
    left[i] = a[p + i]
  end

  0.upto(n2 - 1) do |j|
    right[j] = a[q + 1 + j]
  end

  p.upto(r) do |k|
    return if left.empty? && right.empty?
    a[k] =  if right.empty? && !left.empty?
              left.shift
            elsif left.empty? && !right.empty?
              right.shift
            else
              left.first > right.first ? right.shift : left.shift
            end
  end
end

def merge_sort(a, p = nil, r = nil)
  p, r = 0, a.size - 1 if p.nil? && r.nil?
  return if p >= r

  q = (p + r) / 2
  merge_sort(a, p, q)
  merge_sort(a, q + 1, r)
  merge(a, p, q, r)

  a
end
