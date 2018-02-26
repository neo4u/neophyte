#!/usr/bin/env ruby

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
    next if right.empty? && left.empty?
    array[k] = if right.empty? && !left.empty?
                 left.shift
               elsif left.empty? && !right.empty?
                 right.shift
               else
                 left.first > right.first ? right.shift : left.shift
               end
  end
end

def merge_sort(a, p = nil, r = nil)
  p = 0 if p.nil?
  r = a.size - 1 if r.nil?

  return if p >= r

  q = (p + r) / 2
  merge_sort(a, p, q)
  merge_sort(a, q + 1, r)
  merge(a, p, q, r)

  a
end

# data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
# puts "Before Sort: #{data}"
# merge_sort(data)
# puts "After Sort: #{data}"
# puts "\n"