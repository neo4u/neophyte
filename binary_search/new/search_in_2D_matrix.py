class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None: return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // m][mid % n]
            print(f"low: {low}, high: {high}, mid: {(low + high) // 2}, i: {mid // m}, j: {mid % n}, num: {num}")

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/


sol = Solution()

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
assert sol.searchMatrix(matrix, target) == True

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
assert sol.searchMatrix(matrix, target) == False
