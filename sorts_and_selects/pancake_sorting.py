from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        result = []

        for i in range(n):
            cur_max = max(A[0:n - i])
            j = 0
            while A[j] != cur_max: j += 1

            # should reverse j + 1 elements
            A[:j + 1] = reversed(A[:j + 1])
            result.append(j + 1)

            # reverse all
            A[:n - i] = reversed(A[:n - i])
            result.append(n - i)

        return result


# 969. Pancake Sorting
# https://leetcode.com/problems/pancake-sorting/description/



# Approach 1:

# - Find the largest number, assuming its subscript is i
# - Reverse the number between 0 and i, so that A [i] becomes the first number
# - Reverse the entire array and let the largest number reach the end

# Find the largest element A[i], reverse A[0:i+1], making the current largest at the head of the array, then reverse the whole array to make A[i] at the bottom.
# Do the above again and again, finally we'll have the whole array sorted.
# eg:

# [3,1,4,2] (input array)
# [4,1,3,2] -> [2,3,1,4] (current maximum 4 is placed at the bottom)
# [3,2,1,4] -> [1,2,3,4] (current maximum 3 is placed at the bottom)
# [2,1,3,4] -> [1,2,3,4] (current maximum 2 is placed at the bottom)
# [1,2,3,4] -> [1,2,3,4] (current maximum 1 is placed at the bottom)


# i = 0
# 1,2,5,6,4
#       j
# 6,5,2,1,4       [4, ]

# 4,1,2,5,6       [4, 5]

# i = 1
# 4,1,2,5,6
#       j
# 5,2,1,4,6       [4, 5, 4]
# 4,1,2,5,6       [4, 5, 4, 4]

# i = 2
# 4,1,2,5,6
# j
# 2,1,4,5,6       4, 5, 4, 4, 1, 3]


# i = 3
