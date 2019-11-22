from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        result, l, r = [0] * n, 0, n - 1
        i = n - 1

        while l <= r:
            l_num, r_num = abs(A[l]), abs(A[r])
            if l_num > r_num:
                result[i] = l_num**2
                l += 1
            else:
                result[i] = r_num**2
                r -= 1
            i -= 1

        return result


# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Intuition:
# - High negatives numbers may end up becoming larger than medium size +ve numbers
# - We can start a pointer from back to keep track of curr insertion position into the result array
# - Use 2 pointers l and r to accordingly advance indexes into the array and populate the larger square into the result

# Time: O(n)
# Space: O(1), result array is not counted toward space complexity
