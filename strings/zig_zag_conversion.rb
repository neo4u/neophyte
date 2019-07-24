# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
    return s if nun_rows == 1 || num_rows.size >= s.size

    result = Array.new(num_rows, '')
    row, down = 0, false

    s.each_char do |c|
        result[row] += c
        down = !down if row == 0 || row == nums_rows - 1
        row += down ? 1 : -1
    end

    result.join('')
end

# 6. ZigZag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/

# Complexity Analysis
# Time Complexity: O(n), where n == len(s)
# Space Complexity: O(n)