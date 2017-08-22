#!/usr/bin/env ruby

Dir['../problems/*.rb'].each do |file|
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

  def test_diag_diff
    assert_equal(15, diag_diff([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
  end
end

# --------------------------------------------------------------------
# puts diag_diff([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
# --------------------------------------------------------------------
