#!/usr/bin/env ruby

Dir['../data-structures/*.rb'].each do |file|
  require_relative File.join(File.dirname(file), File.basename(file, File.extname(file)))
end
require 'test/unit'
require 'set'

class ADTTests < Test::Unit::TestCase
  def rand_n(n, max)
    randoms = Set.new
    loop do
      randoms << rand(max)
      return randoms.to_a if randoms.size >= n
    end
  end

  def test_bin_heap
    a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    excepted_result = [11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2]
    heap = BinaryMaxHeap.new(a)
    assert_equal(excepted_result, heap.data)
    assert_equal([25, 9, 11, 7, 6, 10, 8, 3, 1, 4, 0, 2, 5], heap.insert(25))
    assert_equal(-4611686018427387904, heap.delete(0))
    assert_equal([11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2], heap.data)
    assert_equal(-4611686018427387904, heap.remove(0))
    assert_equal([10, 9, 8, 7, 6, 5, 2, 3, 1, 4, 0], heap.data)
    assert_equal(10, heap.peek)
    assert_equal(10, heap.extract_max)
    assert_equal([9, 7, 8, 3, 6, 5, 2, 0, 1, 4], heap.data)
    assert_equal([35, 7, 9, 3, 6, 5, 8, 0, 1, 4], heap.increase_key(6, 35))
  end
end

# --------------------------------------------------------------------
# Binary Heap
# a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
# heap = BinaryMaxHeap.new(a)
# puts heap.insert(25).inspect
# heap.delete(0)
# heap.show
# heap.remove(0)
# heap.show
# puts heap.peek
# puts heap.extract_max
# heap.show
# heap.increase_key(6, 35)
# heap.show
# --------------------------------------------------------------------
