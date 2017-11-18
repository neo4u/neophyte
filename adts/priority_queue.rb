#!/usr/bin/env ruby

# ------------------------------------------------------------------------
# Binary Heap as per CLRS  THis should be changed to priority queue
# as PQ is the ADT and heap is the data structure
# ------------------------------------------------------------------------
class PriorityQueue
  attr_accessor :data

  def initialize(a)
    @size = a.size
    @data = build_max_heap(a)
  end

  def insert(x)
    alias :add :insert

    @data << x
    i = @size
    sift_up(@data, i)
    @size += 1

    @data
  end

  def delete(i)
    alias :remove :delete
    @data[i] = -Float::INFINITY
    @data[i], @data[-1] = @data[-1], @data[i]
    max_heapify(@data, i, @size)
    @size -= 1

    @data.pop
  end

  def increase_key(i, key)
    @data[i] = key
    sift_up(@data, i)

    @data
  end

  def peek
    alias :max :peek
    @data.first
  end

  def extract_max
    ret = @data[0]

    @data[0] = -Float::INFINITY
    @data[0], @data[-1] = @data[-1], @data[0]
    @data.pop
    @size -= 1
    max_heapify(@data, 0, @size)

    ret
  end

  def show
    puts "Data: #{@data}"
  end

  private

  def build_max_heap(a)
    ((a.size - 2) / 2).downto(0) do |i|
      max_heapify(a, i, a.size)
    end

    a
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
    return if largest == i
    a[i], a[largest] = a[largest], a[i]

    max_heapify(a, largest, heapsize)
  end

  def left_child(i)
    2 * i + 1
  end

  def right_child(i)
    2 * i + 2
  end

  def parent(i)
    (i - 1) / 2
  end

  def sift_up(a, i)
    while a[parent(i)] < a[i] && parent(i) >= 0
      a[parent(i)], a[i] = a[i], a[parent(i)]
      i = parent(i)
    end
  end
end
