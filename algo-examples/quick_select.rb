#!/usr/bin/env ruby

def partition(a, p, r)
  i = p - 1                       # Choose the index before the pth index
  pivot = a[r]                    # Choose the last element as pivot

  (p...r).each do |j|             # Loop from p to r-1 moving elements to either side of pivot
    next if a[j] > pivot          # Move to next element if array element greater than pivot
    i += 1                        # Increment index i for current placement index
    a[i], a[j] = a[j], a[i]       # Swap elements at pivot placement index with the current index j
  end

  a[i + 1], a[r] = a[r], a[i + 1] # Move the pivot to its final place: index before which all elements < pivot
  i + 1                           # return pivot index
end

def rand_partition(a, p, r)
  i = rand(p..r)            # Pick a random index between p and r
  a[i], a[r] = a[r], a[i]   # Swap the last element with the on at i

  partition(a, p, r)        # Return result of partition()
end

def rand_quick_sort(a, p, r)
  return if p >= r

  q = rand_partition(a, p, r)
  rand_quick_sort(a, p, q - 1)
  rand_quick_sort(a, q + 1, r)
  a
end

def quick_select(a, p, r, i)
  return a[p] if p == r                             # Base case of recursion
  q = rand_partition(a, p, r)                       # Pick the pivot using random partition

  return a[q] if q == i                             # Return Pivot as the ith smallest
  return quick_select(a, p, q - 1, i) if q > i      # ith smallest is in the lower partition
  quick_select(a, q + 1, r, i)                      # ith smallest is in the higher partition
end

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9].shuffle
# puts "Before Quickselect: #{a}"
# puts "array is #{rand_quick_sort(a, 0, a.size - 1)}"
# puts quick_select(a, 0, a.size - 1, 0)

require 'test/unit'
extend Test::Unit::Assertions

a = [3,2,1,5,6,4]
# a.each_index { |i| assert_equal(quick_select(a, 0, a.size - 1, 1), i + 1) }
assert_equal(quick_select(a, 0, a.size - 1, 1), 2)