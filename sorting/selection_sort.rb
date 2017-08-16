#!/usr/bin/env ruby

def selection_sort(data)
  0.upto(data.count - 1) do |i|
    min_idx = i
    (i + 1).upto(n) { |j| min_idx = j if data[j] < data[min_idx] }
    data[i], data[min_idx] = data[min_idx], data[i] unless min_idx.eql?(i)
  end
end

data = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
puts "Before Sort: #{data}"
selection_sort(data)
puts "After Sort: #{data}"
puts "\n"

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
puts "Before Sort: #{data}"
selection_sort(data)
puts "After Sort: #{data}"
puts "\n"

data = [0, 1, 2, 2, 3, 4, 4, 7, 8, 9, 11, 10]
puts "Before Sort: #{data}"
selection_sort(data)
puts "After Sort: #{data}"
puts "\n"

data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
puts "Before Sort: #{data}"
selection_sort(data)
puts "After Sort: #{data}"
puts "\n"
