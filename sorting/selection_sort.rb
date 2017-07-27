#!/usr/bin/env ruby

# --------------------------------------------------------------------------------
# Selection Sort
# --------------------------------------------------------------------------------
def selection_sort(data)
  n = data.count

  0.upto(n - 1) do |i|
    min_idx = i
    (i + 1).upto(n - 1) { |j| min_idx = j if data[j] < data[min_idx] }
    # puts "data is: #{data}"; puts "data[i] is #{data[i]}"; puts "data[min_idx] is #{data[min_idx]}"
    data[i], data[min_idx] = data[min_idx], data[i] # unless min.eql?(i)
  end
end


data = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
selection_sort(data)
puts "Data is: #{data}"

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
selection_sort(data)
puts "Data is: #{data}"
