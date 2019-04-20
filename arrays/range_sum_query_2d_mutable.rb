# private int[][] dp;

# public NumMatrix(int[][] matrix) {
#     if (matrix.length == 0 || matrix[0].length == 0) return;
#     dp = new int[matrix.length + 1][matrix[0].length + 1];
#     for (int r = 0; r < matrix.length; r++) {
#         for (int c = 0; c < matrix[0].length; c++) {
#             dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1] + matrix[r][c] - dp[r][c];
#         }
#     }
# }

# public int sumRegion(int row1, int col1, int row2, int col2) {
#     return dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1];
# }
class NumMatrix
    def initialize(matrix)
        return if !matrix || matrix.empty?
        m, n = matrix.size, matrix[0].size
        @sums = Array.new(m + 1) { Array.new(n + 1, 0) }

        1.upto(m) do |i|
            1.upto(n) do |j|
                @sums[i][j] = matrix[i - 1][j - 1] + \
                              @sums[i][j - 1] + \
                              @sums[i - 1][j] - \
                              @sums[i - 1][j - 1]
            end
        end
    end

    def sum_region(row1, col1, row2, col2)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return @sums[row2][col2] - \
               @sums[row2][col1 - 1] - \
               @sums[row1 - 1][col2] + \
               @sums[row1 - 1][col1 - 1]
    end
end


# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/


# Approach 1: Brute-Force
# Approach 2: Caching and updating all rows
# Approach 3: Smart Caching and updating only grid from cell as origin upto n-1,n-1

# Time: O(1) time per query, O(mn) time pre-computation.
#       The pre-computation in the constructor takes O(mn) time.
#       Each sumRegion query takes O(1) time.
# Space: O(mn). The algorithm uses O(mn) space to store the cumulative region sum.


require 'test/unit'
extend Test::Unit::Assertions

