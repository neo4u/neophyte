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

  return if p >= r

  q = (p + r) / 2
  merge_sort(array, p, q)
  merge_sort(array, q + 1, r)
  merge(array, p, q, r)

  array
end
