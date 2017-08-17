#!/usr/bin/env ruby

def parent(i)
  (i - 1) / 2
end

def left_child(i)
  2 * i + 1
end

def right_child(i)
  2 * i + 2
end

def max_heapify(a, i, heapsize)
  l = left_child(i)
  r = right_child(i)
  largest = if l < heapsize && a[l] > a[i]
              l
            else
              i
            end
  largest = r if r < heapsize && a[r] > a[largest]

  return if i.eql?(largest)

  a[i], a[largest] = a[largest], a[i]
  max_heapify(a, largest, heapsize)
end

def build_max_heap(a, heapsize)
  ((a.size - 2) / 2).downto(0) do |i|
    max_heapify(a, i, heapsize)
  end
end

def heap_sort(a)
  heapsize = a.size
  build_max_heap(a, heapsize)
  (a.size - 1).downto(1) do |i|
    a[i], a[0] = a[0], a[i]
    heapsize -= 1
    max_heapify(a, 0, heapsize)
  end

  a
end


