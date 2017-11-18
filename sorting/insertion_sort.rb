#!/usr/bin/env ruby

def insertion_sort(a)
  (1...a.size).each do |j|
    key, i = a[j], j - 1
    while key < a[i] && i >= 0
      a[i + 1] = a[i]
      i -= 1
    end
    a[i + 1] = key unless j == i + 1 # unless its already in place
  end

  a
end
