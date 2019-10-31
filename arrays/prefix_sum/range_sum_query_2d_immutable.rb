class NumMatrix
    def initialize(matrix)
        return if !matrix || matrix.empty?
        m, n = matrix.size, matrix[0].size
        @sums = Array.new(m + 1) { Array.new(n + 1, 0) }

        1.upto(m) do |i|
            1.upto(n) do |j|
                # curr element + 
                # add region from origin upto prev col same row
                # add region from origin upto prev row same col
                # subtract region from origin to prev row prev col
                @sums[i][j] = matrix[i - 1][j - 1] + \
                              @sums[i][j - 1] + \
                              @sums[i - 1][j] - \
                              @sums[i - 1][j - 1]

            end
        end
    end

    def sum_region(row1, col1, row2, col2)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        # Queried region is ABCD points
        # take origin to bottom row right most column (OD)
        # Subtract region from origin to bottom row left most column (OC)
        # Subtract region from origin to top row right most column (OB)
        # Add region origin top row left column (OA) (Bcuz it was remove twice as part OC and OB)

        return @sums[row2][col2] - \
               @sums[row2][col1 - 1] - \
               @sums[row1 - 1][col2] + \
               @sums[row1 - 1][col1 - 1]
    end
end


# @sums[i][j - 1]
# 1 1 0 0
# 1 1 0 0
# 1 1 x 0

# @sums[i][j - 1]
# 1 1 1 0 
# 1 1 1 0
# 0 0 x 0 

# @sums[i - 1][j - 1]
# 1 1 0 0 
# 1 1 0 0
# 0 0 x 0


# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/


# Approach 1: Brute-Force
# Approach 2: Caching and updating all rows
# Approach 3: Smart Caching and updating only grid from cell as origin upto n-1,n-1

# Time: O(1) time per query, O(mn) time pre-computation.
#       The pre-computation in the constructor takes O(mn) time.
#       Each sumRegion query takes O(1) time.
# Space: O(mn). The algorithm uses O(mn) space to store the cumulative region sum.

