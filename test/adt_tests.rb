#!/usr/bin/env ruby

require_relative '../adts/priority_queue'
require 'test/unit'

class ADTTests < Test::Unit::TestCase
  def test_priority_queue
    a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    excepted_result = [11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2]
    q = PriorityQueue.new(a)
    assert_equal(excepted_result, q.data)
    assert_equal([25, 9, 11, 7, 6, 10, 8, 3, 1, 4, 0, 2, 5], q.insert(25))
    assert_equal(-Float::INFINITY, q.delete(0))
    assert_equal([11, 9, 10, 7, 6, 5, 8, 3, 1, 4, 0, 2], q.data)
    assert_equal(-Float::INFINITY, q.remove(0))
    assert_equal([10, 9, 8, 7, 6, 5, 2, 3, 1, 4, 0], q.data)
    assert_equal(10, q.peek)
    assert_equal(10, q.extract_max)
    assert_equal([9, 7, 8, 3, 6, 5, 2, 0, 1, 4], q.data)
    assert_equal([35, 7, 9, 3, 6, 5, 8, 0, 1, 4], q.increase_key(6, 35))
  end
end

# --------------------------------------------------------------------
# Binary Heap
# a = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
# heap = PriorityQueue.new(a)
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
