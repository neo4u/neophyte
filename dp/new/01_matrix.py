# We simply do 2 iterations from first to last and last to first element.
# For the 1st for loop, we update distance of element with minimum of previous top and left elements + 1 (itself).
# For the 2nd for loop, we update distance of element with minimum of previous bottom and right elements + 1 (itself).
# As a result, we get minimum distance value for each element updated with distances of neighbours + 1.
class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix

# For this question, we only need to consider 4 direction, up, down ,left and right.
# so, first, I go through this matrix from top-left to down-right, and we can find the minimum distance from up and left, then, go through the matrix from down-right to top-left, so we can find the minimum distance from down and right. and it said the elements will not exceed 10,000, so I just set the initial value as 10,000.

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        if not matrix or not matrix[0]:
            return matrix
        h,w = len(matrix),len(matrix[0])
        mask = [[10000]*w for i in xrange (h)]
        for i in xrange (h):
            for j in xrange (w):
                if matrix[i][j] != 0:
                    mask[i][j] = min(mask[i][j],mask[i-1][j]+1,mask[i][j-1]+1)
                else:
                    mask[i][j] = 0
        for i in xrange (h-1,-1,-1):
            for j in xrange (w-1,-1,-1):
                if matrix[i][j] != 0:
                    if i < h-1:
                        mask[i][j] = min(mask[i][j],mask[i+1][j] + 1)
                    if j < w-1:
                        mask[i][j] = min(mask[i][j],mask[i][j+1] + 1)
        return mask
If you have any better idea, please let me know! Thanks!