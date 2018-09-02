#!/usr/bin/env ruby

def selection_sort(a)
  0.upto(a.size - 2) do |i|
    min_idx = i
    (i + 1).upto(a.size - 1) { |j| min_idx = j if a[j] < a[min_idx] }
    a[min_idx], a[i] = a[i], a[min_idx]
  end

  a
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(selection_sort([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
assert_equal(selection_sort([7,6,5,4,3,2,1]), [1,2,3,4,5,6,7])
assert_equal(selection_sort([7,6,5,4,3,2,2,2,2,2,1]), [1,2,2,2,2,2,3,4,5,6,7])
