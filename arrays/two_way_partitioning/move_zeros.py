from typing import List


# Approach: Two Pointer
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p_idx = 0

        for i, num in enumerate(nums):
            if num == 0: continue   # If curr num == 0, its already after the non-zero idx, so go to next num
            nums[p_idx], nums[i] = nums[i], nums[p_idx]
            p_idx += 1

    # Variant: Move all zeros to the front of the list
    def moveZeroesFront(self, nums: List[int]) -> None:
        n = len(nums)
        p_idx = n - 1

        for i in reversed(range(n)):
            if nums[i] == 0: continue   # If curr num == 0, its already after the non-zero idx, so go to next num
            nums[p_idx], nums[i] = nums[i], nums[p_idx]
            p_idx -= 1


# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/


# Intuition:
# 1. We need to move all non-zero elements to 1-side and zero elements, interviewer can ask either side (Very Important)
# 2. We need to maintain the relative order of the non-zero elements (Also a requirement from interviews)
# 3. Don't worry about the non-zero elements, look for non-zero elements
#    and swap them with the element at a partition index which marks where the zero elements start
#    and non-zero elements end, initially this is set to p_idx = 0, cuz all elements are to be categorized

# Approach: Two Pointer
# 1. Keep the partition index which marks the start the first zero
# 2. Each time you get a non-zero element swap with the first zero index

# Time: O(n)
# Space: O(1)


sol = Solution()
arr = [0, 1, 0, 3, 12]
sol.moveZeroes(arr)
assert arr == [1, 3, 12, 0, 0]

arr = [0, 0, 1]
sol.moveZeroes(arr)
assert arr == [1, 0, 0]

# Variant: To move zeros to the front
arr = [0, 1, 0, 3, 12]
sol.moveZeroesFront(arr)
assert arr == [0, 0, 1, 3, 12]

arr = [0, 0, 1]
sol.moveZeroesFront(arr)
assert arr == [0, 0, 1]
