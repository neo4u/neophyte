# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    result = []
    curr_row, prev_row = nil, nil
    0.upto(num_rows - 1) do |i|
        curr_row = []
        0.upto(i) do |j|
            curr_row.push([i, 0].include?(j) ? 1 : prev_row[j - 1] + prev_row[j])
        end
        prev_row = curr_row
        result.push(curr_row)
    end

    result
end

# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/

require 'test/unit'
extend Test::Unit::Assertions

three_answer = [[1],[1,1],[1,2,1]]
four_answer = [[1],[1,1],[1,2,1],[1,3,3,1]]
five_answer = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

assert_equal(generate(3), three_answer)
assert_equal(generate(4), four_answer)
assert_equal(generate(5), five_answer)