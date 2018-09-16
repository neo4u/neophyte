# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
    return 0 if matrix.empty? || !matrix
    n = matrix[0].size
    max_area, heights = 0, [0] * n
    
    matrix.each do |row|
        0.upto(n - 1) do |i|
            heights[i] += 1 if row[i] == '1'
        end

        max_area = [max_area, largest_rectangle_area(heights)].max
    end

    max_area
end

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


matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

# O(n**2)
# https://leetcode.com/problems/maximal-rectangle/description/
# 85. Maximal Rectangle

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(maximal_rectangle(matrix), 6)
