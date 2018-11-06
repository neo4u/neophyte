class NumMatrix

=begin
    :type matrix: Integer[][]
=end
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

=begin
    :type row1: Integer
    :type col1: Integer
    :type row2: Integer
    :type col2: Integer
    :rtype: Integer
=end
    def sum_region(row1, col1, row2, col2)
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return @sums[row2][col2] - \
               @sums[row2][col1 - 1] - \
               @sums[row1 - 1][col2] + \
               @sums[row1 - 1][col1 - 1]
    end
end

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix.new(matrix)
# param_1 = obj.sum_region(row1, col1, row2, col2)


# Construct a 2D array sums[row+1][col+1]

# (notice: we add additional blank row sums[0][col+1]={0} and
# blank column sums[row+1][0]={0} to remove the edge case checking),
# so, we can have the following definition
# sums[i+1][j+1] represents the sum of area from matrix[0][0] to matrix[i][j]
# To calculate sums, the ideas as below

# +-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
# |     | |       |     |        |     |     |     |         |     |     |        |
# |     | |       |     |        |     |     |     |         |     |     |        |
# +-----+-+       |     +--------+     |     |     |         |     +-----+        |
# |     | |       |  =  |              |  +  |     |         |  -  |              |
# +-----+-+       |     |              |     +-----+         |     |              |
# |               |     |              |     |               |     |              |
# |               |     |              |     |               |     |              |
# +---------------+     +--------------+     +---------------+     +--------------+

#    sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]   +  
#                         matrix[i-1][j-1]
# So, we use the same idea to find the specific area's sum.

# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
# |               |   |         |    |   |   |           |   |         |    |   |   |          |
# |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
# |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
# |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
# |   |      |    |   |         |    |   |   |           |   |              |   |              |
# |   +------+    |   +---------+    |   +---+           |   |              |   |              |
# |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
# +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
# And we can have the following code
