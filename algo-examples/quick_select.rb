#!/usr/bin/env ruby

def partition(a, left, right)
  i = left                        # Choose the index before the pth index
  pivot = a[right]                # Choose the last element as pivot
  left.upto(right - 1) do |j|     # Loop from p to r-1 moving elements to either side of pivot
    if a[j] <= pivot              # Move to next element if array element greater than pivot
      a[i], a[j] = a[j], a[i]     # Swap elements at pivot placement index with the current index j
      i += 1                      # Increment index i for current placement index
    end
  end
  a[i], a[right] = a[right], a[i] # Move the pivot to its final place: index after which elements < pivot
  i                               # return pivot index
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
  puts "quick_select called with left: #{p} r: #{r} i: #{i}"
  return a[p] if p == r                             # Base case of recursion

  q = rand_partition(a, p, r)                       # Pick the pivot using random partition
  puts "Pivot index is: #{q}"
  puts "Array is: #{a}"
  # i = q                                             # Size of the partition less than pivot
  return a[q] if q == i                             # Pivot is the ith smallest
  return quick_select(a, p, q - 1, i) if q < i      # ith smallest is in the lower partition

  quick_select(a, q + 1, r, i)                      # ith smallest is in the higher partition
end

a = [1, 2, 3, 4, 5, 6, 7, 8, 9].shuffle
puts "Before Quickselect: #{a}"
puts "array is #{rand_quick_sort(a, 0, a.size - 1)}"
puts quick_select(a, 0, a.size - 1, 4)
# def quickselect(a, k)
#   arr = a.dup # we will be modifying it

#   pivot = arr.delete_at(rand(arr.length))
#   left, right = arr.partition { |x| x < pivot }
#   if k == left.length
#     return pivot
#   elsif k < left.length
#     arr = left
#     return quickselect(arr, k)
#   else
#     k = k - left.length - 1
#     arr = right
#     return quickselect(arr, k)
#   end
# end

# v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
# p v.each_index.map { |i| quickselect(v, i) }
