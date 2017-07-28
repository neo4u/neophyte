#!/usr/bin/env ruby

def insertion_sort(data)
  (1...data.count).each do |i|
    j = i - 1
    element = data[i]
    while element < data[j] && j >= 0
      data[j + 1] = data[j]
      j -= 1
    end
    data[j + 1] = element
  end
end

data = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
puts "Before Sort: #{data}"
insertion_sort(data)
puts "After Sort: #{data}"
puts "\n"

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
puts "Before Sort: #{data}"
insertion_sort(data)
puts "After Sort: #{data}"
puts "\n"

data = [0, 1, 2, 2, 3, 4, 4, 7, 8, 9, 11, 10]
puts "Before Sort: #{data}"
insertion_sort(data)
puts "After Sort: #{data}"
puts "\n"

data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
puts "Before Sort: #{data}"
insertion_sort(data)
puts "After Sort: #{data}"
puts "\n"
