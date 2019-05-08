class Solution:
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        while hi >= lo:
            mid = (lo + hi) // 2
            if vertical:  # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:  # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        # iterate over matrix diagonals starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True

        return False

# Fastest Python solution
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0: return False

        n = len(matrix[0])
        X = [(0, 0, m - 1, n - 1)]

        while X:
            i, j, k, l = X.pop()
            if i > k or j > l or \
                matrix[i][j] > target or matrix[k][l] < target:
                    continue

            p, q = (i + k)// 2, (j + l) // 2
            if matrix[p][q] == target: return True

            if matrix[p][q] < target:
                X += [(p + 1, j, k, q), (0, q + 1, k, l)]
            else:
                X += [(i, j, k, q - 1), (0, q, p - 1, l)]

        return False





# 240. Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Approach 1: Virtually convert a single array and use binary search
# Approach 2: 2D Binary Search
