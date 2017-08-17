#!/usr/bin/env ruby

def insertion_sort(a)
  (1...a.size).each do |j|
    key = a[j]
    i = j - 1
    while key < a[i] && i >= 0
      a[i + 1] = a[i]
      i -= 1
    end
    a[i + 1] = key unless j.eql?(i + 1) # its already in place
  end

  a
end


# data = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
# puts "Before Sort: #{data}"
# insertion_sort(data)
# puts "After Sort: #{data}"
# puts "\n"

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
# puts "Before Sort: #{data}"
# insertion_sort(data)
# puts "After Sort: #{data}"
# puts "\n"

# data = [0, 1, 2, 2, 3, 4, 4, 7, 8, 9, 11, 10]
# puts "Before Sort: #{data}"
# insertion_sort(data)
# puts "After Sort: #{data}"
# puts "\n"

# data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
# puts "Before Sort: #{data}"
# insertion_sort(data)
# puts "After Sort: #{data}"
# puts "\n"
