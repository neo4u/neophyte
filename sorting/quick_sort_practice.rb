def quick_sort_prac(a, p = nil, r = nil)
  p = 0 if p.nil?
  r = a.size - 1 if r.nil?
  return if p >= r

  q = partition(a, p, r)
  quick_sort_prac(a, p, q - 1)
  quick_sort_prac(a, q + 1, r)

  a
end

def partition(a, p, r)
  i, pivot = p - 1, a[r]
  p.upto(r - 1) do |j|
    next if a[j] > pivot
    i += 1
    a[i], a[j] = a[j], a[i]
  end
  a[i + 1], a[r] = a[r], a[i + 1]

  i + 1
end
