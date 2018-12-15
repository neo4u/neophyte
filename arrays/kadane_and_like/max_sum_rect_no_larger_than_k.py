# import bisect
# import sys
# class Solution(object):
#     def maxSumSubmatrix(self, matrix, k):
#         """
#         :type matrix: List[List[int]]
#         :type k: int
#         :rtype: int
#         """
#         if len(matrix) == 0:
#             return 0
#         m, n, res = len(matrix), len(matrix[0]), float("-inf")
#         for left in range(n):
#             sums = [0] * m

#             for right in range(left, n):
#                 for i in range(m):
#                     sums[i] += matrix[i][right]
#                 treeSet = [0]
#                 curSum = 0

#                 for sum in sums:
#                     curSum += sum
#                     i = bisect.bisect_left(treeSet, curSum - k)
#                     if i != len(treeSet):
#                         res = max(res, curSum - treeSet[i])
#                     bisect.insort(treeSet, curSum)
                    
#         return res

import bisect
import sys

class Solution(object):
    def max_sum_no_more_than_k(self, a, k):
        cum_list = [0]
        cum = 0
        max_so_far = -sys.maxint

        for i in range(len(a)):
            cum += a[i]
            cum_j_index = bisect.bisect_left(cum_list, cum - k)  # if bisect_left, no larger than k
            if cum_j_index < len(cum_list):
                max_so_far = max(max_so_far, cum - cum_list[cum_j_index])
            bisect.insort(cum_list, cum)

        return max_so_far

    def maxSumSubmatrix(self, matrix, k):
        if len(matrix)==0:
            return 0

        row_num = len(matrix)
        max_so_far = -sys.maxint
        columns = zip(*matrix)

        for l in range(len(columns)):
            current = [0]*row_num
            for colunm in columns[l:]:
                current = map(int.__add__, current, colunm)
                ans = self.max_sum_no_more_than_k(current, k)
                max_so_far = max(max_so_far, ans)

        return max_so_far
