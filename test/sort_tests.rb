#!/usr/bin/env ruby

# To execute a certain test do
# ./sort_tests.rb -n test_quick_sort

Dir['../sorting/*.rb'].each do |file|
  require_relative File.join(File.dirname(file), File.basename(file, File.extname(file)))
end
require 'test/unit'

class SortTests < Test::Unit::TestCase
  def test_merge_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], merge_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], merge_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
  end

  def test_insertion_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], insertion_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
  end

  def test_selection_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], selection_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], selection_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], selection_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 11]))
    assert_equal([-10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11], selection_sort([0, 1, 2, 3, 4, 5, 6, 7, -10, 9, 0, 11]))
    assert_equal([-50_000, 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11], selection_sort([0, 1, 2, 3, 4, -50_000, 6, 7, 8, 9, 10, 11]))
  end

  def test_heap_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], heap_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], heap_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
  end

  def test_quick_sort
    assert_equal([1, 2, 3, 4, 5, 6, 7, 8], quick_sort([5, 6, 7, 8, 1, 2, 3, 4]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([0, 1, 6, 5, 4, 3, 2, 7, 8, 9, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([0, 1, 2, 3, 4, 9, 8, 7, 6, 5, 10, 11]))
    assert_equal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], quick_sort([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
  end
end
