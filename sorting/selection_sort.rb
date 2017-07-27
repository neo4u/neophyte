#!/usr/bin/env ruby


# --------------------------------------------------------------------------------
# Selection Sort
# -------------------------------------------------------------------------------- 
class SelectionSorter

  def sort(data)
    n = data.count
    0.upto(n - 1) do |i|
      puts "i: #{i}"
      min = i
      (i + 1).upto(n - 1) do |j|
        puts "j: #{j}"
        min = j if data[j] < data[min]
      end
      puts "data is: #{data}"
      puts "data[i] is #{data[i]}"
      puts "data[min] is #{data[min]}"

      data[i], data[min] = data[min], data[i]
    end
  end
end

data = [10, 4, 1, 2, 8, 3, 7, 5, 0, 6, 9]
sorter = SelectionSorter.new
sorter.sort(data)

puts "Data is: #{data}"
