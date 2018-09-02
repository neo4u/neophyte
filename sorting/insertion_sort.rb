#!/usr/bin/env ruby

def insertion_sort(a)
  1.upto(a.size - 1) do |j|
    i, key = j, a[j]

    a[i + 1] = a[i] while (i -= 1) >= 0 && key < a[i] # The (i -= 1) in while condition is equivalent to initializing i = j - 1
    a[i + 1] = key unless i == j - 1 # Note that a[i + 1] from above is different from a[i + 1] in this statement as i -= 1 was done
  end

  a
end


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(insertion_sort([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
assert_equal(insertion_sort([7,6,5,4,3,2,1]), [1,2,3,4,5,6,7])
assert_equal(insertion_sort([7,6,5,4,3,2,2,2,2,2,1]), [1,2,2,2,2,2,3,4,5,6,7])
