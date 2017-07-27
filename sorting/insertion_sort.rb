#!/usr/bin/env ruby

def insertion_sort(data)
  1.upto(data.count - 1) do |i|
    i.downto(1) do |j|
      break if data[j] >= data[j - 1]
      data[j], data[j - 1] = data[j - 1], data[j]
    end
  end
end

data = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
insertion_sort(data)
puts "Data is: #{data}"

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
insertion_sort(data)
puts "Data is: #{data}"

data = [0, 1, 2, 2, 3, 4, 4, 7, 8, 9, 11, 10]
insertion_sort(data)
puts "Data is: #{data}"

data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
insertion_sort(data)
puts "Data is: #{data}"
