#!/usr/bin/env ruby

# -------------------------------------------------------------------------------
# We use indexing from 0 as opposed to CLRS which is mathematical and uses indexing
# from 1 and is confusing as hell
# -------------------------------------------------------------------------------
def parent(i)
  (i - 1) / 2
end

def left_child(i)
  2 * i + 1
end

def right_child(i)
  2 * i + 2
end

# -------------------------------------------------------------------------------
# Ensure that the heap rooted at i satisfies the max-heap property
#   a[parent(i)] >= a[i]
# Recursively call the max_heapify because there is a swap which may cause the
# above property to fail at the tree rooted at the new largest
# -------------------------------------------------------------------------------
def max_heapify(a, i, heapsize)
  l = left_child(i)
  r = right_child(i)
  largest = if l < heapsize && a[l] > a[i]
              l
            else
              i
            end
  largest = r if r < heapsize && a[r] > a[largest]
  return if i == largest

  a[i], a[largest] = a[largest], a[i]
  max_heapify(a, largest, heapsize)
end

def build_max_heap(a, heapsize)
  ((heapsize - 2) / 2).downto(0) do |i|
    max_heapify(a, i, heapsize)
  end
end

# -------------------------------------------------------------------------------
# Since the max element of max heap is at the start. We extract the max element
# and place it outside the heap at its final sorted position. We do this for
# heapsize starting from the full heap to a size of 2
# -------------------------------------------------------------------------------
def heap_sort(a)
  heapsize = a.size
  build_max_heap(a, heapsize)
  (heapsize - 1).downto(1) do |i|
    a[i], a[0] = a[0], a[i]
    heapsize -= 1
    max_heapify(a, 0, heapsize)
  end

  a
end
