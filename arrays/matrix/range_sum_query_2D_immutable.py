class NumMatrix(object):
      def __init__(self, matrix):
          if matrix is None or not matrix:
              return
          n, m = len(matrix), len(matrix[0])
          self.sums = [ [0 for j in xrange(m+1)] for i in xrange(n+1) ]
          for i in xrange(1, n+1):
              for j in xrange(1, m+1):
                  self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]
    

      def sumRegion(self, row1, col1, row2, col2):
          row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
          return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]


# The idea is simple, just precompute sums
# for all matrices with (0, 0) as top left corner and (i, j)
# as bottom right corner. There are O(n^2) of these matrices,
# so we store them in a 2D table. In order to make code simpler,
# I add an extra column and row, filled with 0.
