from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rA, cA, cB = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(cB)] for _ in range(rA)]

        for i in range(rA):
            for k in range(cA):
                if A[i][k] == 0: continue
                for j in range(cB):
                    if B[k][j] == 0: continue
                    C[i][j] += A[i][k] * B[k][j]

        return C


# 311. Sparse Matrix Multiplication
# https://leetcode.com/problems/sparse-matrix-multiplication/description/

# i = 0
# 1 2 3     1 4
# 4 5 6     2 5
#           3 6

# 14 32
# x  x

# # input two matrices of size n x m 
# matrix1 = [[12,7,3],
#            [4 ,5,6],
#            [7 ,8,9]]
# matrix2 = [[5,8,1],
#            [6,7,3],
#            [4,5,9]]
  
# res = [[0 for x in range(3)] for y in range(3)]  
# explicit for loops 
# for i in range(len(matrix1)):
#     for j in range(len(matrix2[0])):
#         for k in range(len(matrix2)):
#             # resulted matrix 
#             res[i][j] += matrix1[i][k] * matrix2[k][j]
# print (res)
