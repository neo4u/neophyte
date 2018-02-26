def insertion_sort_prac(a)
  1.upto(a.size - 1) do |j|
    i, key = j, a[j]
    a[i + 1] = a[i] while (i -= 1) >= 0 && key < a[i] # The (i -= 1) in while condition is equivalent to initializing i = j - 1
    a[i + 1] = key unless j == i + 1
  end
  a
end
