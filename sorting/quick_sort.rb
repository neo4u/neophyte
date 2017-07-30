#!/usr/bin/env ruby

def quick_sort(array, p = nil, r = nil)
  p = 0 if p.eql?(nil)
  r = array.length - 1 if r.eql?(nil)

  return if p >= r

  q = partition(array, p, r)
  quick_sort(array, p, q - 1)
  quick_sort(array, q + 1, r)
end

def partition(array, p, r)
  i = p - 1
  pivot = array[r]
  (p...r).each do |j|
    next if array[j] > pivot
    i += 1
    array[i], array[j] = array[j], array[i]
  end
  array[i + 1], array[r] = array[r], array[i + 1]
  i + 1
end

array = [1, 2, 3, 4, 5, 6, 7, 8]
puts "Before Sort: #{array}"
quick_sort(array)
puts "After Sort: #{array}"
puts

array = [8, 2, 3, 4, 5, 6, 7, 1]
puts "Before Sort: #{array}"
quick_sort(array)
puts "After Sort: #{array}"
puts

array = [4, 5, 6, 7, 1, 2, 3, 5]
puts "Before Sort: #{array}"
quick_sort(array)
puts "After Sort: #{array}"
puts

array = [4, 5, 6, 7, 1, 2, 3, 5]
puts "Before Sort: #{array}"
quick_sort(array)
puts "After Sort: #{array}"
puts
