# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
  heights << -1

  stack, ans = [], 0

  0.upto(heights.length - 1) do |i|
    puts "***#{i}***"
    while !stack.empty? && heights[i] < heights[stack.last]
      h = heights[stack.pop()]
      w =  stack.empty? ? i : i - 1 - stack.last
      ans = [ans, h * w].max
      puts "h: #{h} | w:#{w} | i: #{i} | stack.last: #{stack.last} | ans: #{ans}"
    end
    stack.push(i)
  end

  ans
end

# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(largest_rectangle_area([2,1,5,6,2,3]), 10)
