#!/usr/bin/env ruby

def quick_sort(array, p = nil, r = nil)
  p = 0 if p.eql?(nil)
  r = array.length - 1 if r.eql?(nil)

  return if p >= r

  q = partition(array, p, r)
  quick_sort(array, p, q - 1)
  quick_sort(array, q + 1, r)

  array
end

def partition(a, p, r)
  i = p - 1                       # Choose the index before the pth index
  pivot = a[r]                    # Choose the last element as pivot
  (p...r).each do |j|             # Loop from p to r-1 moving elements to either side of pivot
    next if a[j] > pivot          # Move to next element if array element greater than pivot
    i += 1                        # Increment index i for current placement index
    a[i], a[j] = a[j], a[i]       # Swap elements at pivot placement index with the current index j
  end
  a[i + 1], a[r] = a[r], a[i + 1] # Move the pivot to its final place: index after which elements < pivot
  i + 1                           # return pivot index
end
