# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
    return 0 if !matrix || !matrix[0]
    n = matrix[0].length
    heights, ans = Array.new(n + 1, 0), 0
    
    matrix.each do |row|
        0.upto(n) do |i|
            heights[i] = row[i] == '1' ? heights[i] + 1 : 0
        end
        ans = [ans, largest_rectangle(heights)].max
    end

    ans
end
  
def largest_rectangle(heights)
    stack = []
    ans, n = 0, heights.size
    
    0.upto(n - 1) do |i|
        while !stack.empty? && heights[i] < heights[stack.last]
                h = heights[stack.pop()]
                w = stack.empty? ? i : i - 1 - stack.last
                ans = [ans, h * w].max
        end
        stack.push(i)
    end
  
    ans
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