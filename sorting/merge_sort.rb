#!/usr/bin/env ruby

def merge_sort()

end

def merge(array, p, q, r)
  n1 = q - p + 1
  n2 = r - q

  left = []
  right = []

  (0...n1).each do |i|
    left[i] = array[p + i]
  end

  (0...n2).each do |j|
    right[j] = array[q + 1 + j]
  end

  p.upto(r) do |k|
    return if right.empty? && left.empty?
    array[k] =  if right.empty? && !left.empty?
                  left.shift
                elsif left.empty? && !right.empty?
                  right.shift
                else
                  left.first > right.first ? right.shift : left.shift
                end
  end
end

def merge_sort(array, p = nil, r = nil)
  p = 0 if p.nil?
  r = array.length - 1 if r.nil?

  if p < r
    q = (p + r) / 2
    merge_sort(array, p, q)
    merge_sort(array, q + 1, r)
    merge(array, p, q, r)
  end

end

array = [5, 6, 7, 8, 1, 2, 3, 4]
puts "Before Sort: #{array}"
merge_sort(array)
puts "After Sort: #{array}"
puts "\n"

array = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
puts "Before Sort: #{array}"
merge_sort(array)
puts "After Sort: #{array}"
puts "\n"

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
puts "Before Sort: #{array}"
merge_sort(array)
puts "After Sort: #{array}"
puts "\n"

data = [0, 1, 2, 2, 3, 4, 4, 7, 8, 9, 11, 10]
puts "Before Sort: #{array}"
merge_sort(array)
puts "After Sort: #{array}"
puts "\n"

data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
puts "Before Sort: #{array}"
merge_sort(array)
puts "After Sort: #{array}"
puts "\n"
