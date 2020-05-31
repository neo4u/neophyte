from typing import List


class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if len(A) == 1: return A
        l = len(A) - 2

        while l >= 0:
            if A[l] > A[l + 1]: break                   # 1. Find the first non-decreasing element from right (n - 2th idx)
            l -= 1
        else: return A                                  # 2.1 If it keeps decreasing

        r = len(A) - 1
        while A[r] >= A[l]: r -= 1                      # 3. Find the first value on the right that is less than A[l]
        while r > 0 and A[r] == A[r - 1]: r -= 1        # 4. Slide to the left, if the left side of r is the same as r_val
        A[l], A[r] = A[r], A[l]                         # 5. swap

        return A


# 1053. Previous Permutation With One Swap
# https://leetcode.com/problems/previous-permutation-with-one-swap/description/

# Intuition:
# - Similar to 31. Next Permutation
# - Differs from 31 in that here we want the next smallest, there we're looking for the next smallest lexicographically larger perm
#   Here, we're looking for the next smallest perm


# Approach 1: Greedy


# Time: O(n)
# Space: O(1)


sol = Solution()
assert sol.prevPermOpt1([3,2,1]) == [3,1,2]
# assert sol.prevPermOpt1([1,1,5]) == [1,1,5]
# assert sol.prevPermOpt1([1,9,4,6,7]) == [1,7,4,6,9]
# assert sol.prevPermOpt1([3,1,1,3]) == [1,3,1,3]
