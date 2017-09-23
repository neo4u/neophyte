def insertion_sort(a)
  1.upto(a.size - 1) do |j|
    key = a[j]
    i = j - 1
    while a[i] > key && i >= 0
      a[i + 1] = a[i]
      i -= 1
    end
    a[i + 1] = key unless j == i + 1
  end
end

