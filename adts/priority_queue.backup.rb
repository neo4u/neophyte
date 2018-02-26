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

  end

  def delete(i)
    alias :remove :delete


  end

  def increase_key(i, key)

    @data
  end

  def peek
    alias :max :peek

    @data.first
  end

  def extract_max

    ret
  end

  def show
    puts "Data: #{@data}"
  end

  private

  def build_max_heap(a)


    a
  end

  def max_heapify(a, i, heapsize)

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

  end
end
