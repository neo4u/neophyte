#!/usr/bin/env ruby

def insertion_sort_prac(a)
  (1...a.size).each do |j|
    key = a[j]
    i = j - 1
    while key < a[i] && i >= 0
      a[i + 1] = a[i]
      i -= 1
    end
    a[i + 1] = key unless j.eql?(i + 1) # unless its already in place
  end

  a
end
