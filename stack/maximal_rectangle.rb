# @param {Character[][]} matrix
# @return {Integer}
# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
    return 0 if !matrix || matrix.empty?
    max_area, n = 0, matrix[0].size()
    heights = Array.new(n, 0)

    matrix.each do |row|
        0.upto(n - 1) do |i|
            heights[i] = row[i] == '1' ? heights[i] + 1 : 0 # extend value or reset to zero
        end
        
        max_area = [max_area, largest_rect_area(heights)].max
    end
    
    max_area
end


def largest_rect_area(heights)
    heights << -1 # Force pop at the end of loop for reminents of stack
    max_area, stack, n = 0, [], heights.size()

    0.upto(n - 1) do |i|
        while !stack.empty? && heights[i] < heights[stack.last()]
            h = heights[stack.pop()]
            w = stack.empty? ? i : i - 1 - stack.last()
            max_area = [max_area, h * w].max
        end
        stack.push(i)
    end

    max_area
end


# O(n**2)
# https://leetcode.com/problems/maximal-rectangle/description/
# 85. Maximal Rectangle

require 'test/unit'
extend Test::Unit::Assertions

arr = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
assert_equal(maximal_rectangle(arr), 6)
arr = [['1']]
assert_equal(maximal_rectangle(arr), 1)
arr = [["0", "1"], ["1", "0"]]
assert_equal(maximal_rectangle(arr), 1)