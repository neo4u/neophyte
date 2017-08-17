#!/usr/bin/env ruby

Dir['../sorting/*.rb'].each do |file|
  require_relative File.join(File.dirname(file), File.basename(file, File.extname(file)))
end
require 'test/unit'
require 'set'

class SortTests < Test::Unit::TestCase
  def rand_n(n, max)
    randoms = Set.new
    loop do
      randoms << rand(max)
      return randoms.to_a if randoms.size >= n
    end
  end

  def test_merge_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], merge_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal(rand_n(1_000_000, 1_000_000).sort, merge_sort(rand_n(1_000_000, 1_000_000)))
  end

  def test_insertion_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], insertion_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal(rand_n(1_000_000, 1_000_000).sort, insertion_sort(rand_n(1_000_000, 1_000_000)))
  end

  def test_selection_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], selection_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], selection_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], selection_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], selection_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], selection_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal(rand_n(1_000_000, 1_000_000).sort, selection_sort(rand_n(1_000_000, 1_000_000)))
  end

  def test_heap_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], heap_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal(rand_n(1_000_000, 1_000_000).sort, heap_sort(rand_n(1_000_000, 1_000_000)))
  end

  def test_quick_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], quick_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal(rand_n(1_000_000, 1_000_000).sort, quick_sort(rand_n(1_000_000, 1_000_000)))
  end
end

# Manual Tests for debugging
# data = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
# puts "Before Sort: #{data}"
# heap_sort(data)
# puts "After Sort: #{data}"
# puts "\n"

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
# puts "Before Sort: #{data}"
# heap_sort(data)
# puts "After Sort: #{data}"
# puts "\n"

# data = [0, 1, 2, 2, 3, 4, 4, 7, 8, 9, 11, 10]
# puts "Before Sort: #{data}"
# heap_sort(data)
# puts "After Sort: #{data}"
# puts "\n"

# data = [1, 0, 3, 2, 4, 3, 6, 5, 9, 8, 11, 10]
# puts "Before Sort: #{data}"
# heap_sort(data)
# puts "After Sort: #{data}"
# puts "\n"