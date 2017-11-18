def insertion_sort_prac(a)
  1.upto(a.size - 1) do |j|
    key, i = a[j], j - 1
    while i >= 0 && key < a[i]
      a[i + 1] = a[i]
      i -= 1
    end
    a[i + 1] = key unless j == i + 1
  end
  a
end
