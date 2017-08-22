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

  def test_heap
    assert_equal(15, diag_diff([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
  end
end

# --------------------------------------------------------------------
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
