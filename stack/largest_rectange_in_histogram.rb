# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
    # Add -1 at the end to force a pop of remaining elements in the stack
    heights << -1
    max_area, n, stack = 0, heights.size, []
    
    0.upto(n - 1) do |i|
        while !stack.empty? && heights[i] < heights[stack.last]
            h = heights[stack.pop]
            w = stack.empty? ? i : i - stack.last - 1
            max_area = [max_area, h * w].max
        end
        stack.push(i)
    end

    max_area
end


# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(largest_rectangle_area([2,1,5,6,2,3]), 10)
