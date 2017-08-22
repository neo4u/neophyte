#!/usr/bin/env ruby

def diag_diff(arr)
  lsum = 0
  rsum = 0
  0.upto(arr.size - 1) do |i|
    j = i
    row = arr[i]
    l_x = row[j]
    r_x = row[-(j + 1)]
    lsum += l_x
    rsum += r_x
  end

  (lsum - rsum).abs
end
