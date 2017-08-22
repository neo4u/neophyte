#!/usr/bin/env ruby

# ------------------------------------------------------------------------
# Binary Heap as per CLRS
# ------------------------------------------------------------------------
class BinaryMaxHeap

  SINGLE_INT_BYTES = 0.size
  SINGLE_INT_BITS = SINGLE_INT_BYTES * 8
  FIXNUM_MAX = 2**(SINGLE_INT_BITS - 2) - 1
  FIXNUM_MIN = -FIXNUM_MAX - 1

  def initialize(a)
    @size = a.size
    @data = self.class.build_max_heap(a)
  end

  def self.build_max_heap(a)
    puts "Building max heap for the first time."
    ((a.size - 2) / 2).downto(0) do |i|
      max_heapify(a, i, a.size)
    end

    a
  end

  def self.max_heapify(a, i, heapsize)
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

  def self.left_child(i)
    2 * i + 1
  end

  def self.right_child(i)
    2 * i + 2
  end

  def self.parent(i)
    (i - 1) / 2
  end

  def self.sift_up(a, i)
    while a[parent(i)] < a[i] && parent(i) >= 0
      a[parent(i)], a[i] = a[i], a[parent(i)]
      i = parent(i)
    end
  end

  def insert(x)
    alias :add :insert

    @data << x
    i = @size
    self.class.sift_up(@data, i)
    @size += 1

    @data
  end

  def delete(i)
    alias :remove :delete

    @data[i] = FIXNUM_MIN
    @data[i], @data[-1] = @data[-1], @data[i]
    self.class.max_heapify(@data, i, @size)
    @size -= 1

    @data.pop
  end

  def increase_key(i, key)
    @data[i] = key
    self.class.sift_up(@data, i)
  end

  def peek
    alias :max :peek

    @data.first
  end

  def extract_max
    ret = @data.first

    @data[0] = FIXNUM_MIN
    @data[0], @data[-1] = @data[-1], @data[0]
    @data.pop
    @size -= 1
    self.class.max_heapify(@data, 0, @size)

    ret
  end

  def show
    puts "Data: #{@data}"
  end
end

