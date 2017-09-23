
def selection_sort_prac(a)
  0.upto(a.size - 1) do |i|
    min_idx = i
    i.upto(a.size - 1) { |j| min_idx = j if a[j] < a[min_idx] }
    a[i], a[min_idx] = a[min_idx], a[i] unless i == min_idx
  end

  a
end
