#!/usr/bin/env ruby

def selection_sort(data)
  0.upto(data.size - 1) do |i|
    min_idx = i
    (i + 1).upto(data.size - 1) { |j| min_idx = j if data[j] < data[min_idx] }
    data[i], data[min_idx] = data[min_idx], data[i] unless min_idx.eql?(i)
  end

  data
end
