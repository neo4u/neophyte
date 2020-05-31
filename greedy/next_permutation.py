from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if len(nums) == 1: return

        l = n - 2
        while l >= 0:
            if nums[l] < nums[l + 1]: break
            l -= 1
        else:
            self.reverse(nums, 0, n - 1)
            return

        r = n - 1
        while nums[r] <= nums[l]: r -= 1                      # 3. Find the first value on the right that is > A[l]
        nums[l], nums[r] = nums[r], nums[l]                   # 5. swap
        self.reverse(nums, l + 1, n - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1



class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        r = n - 1

        while r > 0 and nums[r] <= nums[r - 1]: r -= 1  # Find the first decreasing element from right to left
        if r == 0: return self.reverse(nums, 0, n - 1)  # Rerturn reverse of array if non-decreasing

        pivot_idx, to_replace = r - 1, 0
        for i in range(n - 1, pivot_idx, -1):           # to find the smallest element > nums[pivot_idx]
            if nums[i] <= nums[pivot_idx]: continue
            to_replace = i
            break

        nums[pivot_idx], nums[to_replace] = nums[to_replace], nums[pivot_idx]
        self.reverse(nums, pivot_idx + 1, n - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1


# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/description/


# Intuition:
# Similar to 1053. Previous Permutation With One Swap. But opposite in terms of what we're scanning from the right to left

# You have to find the next greater permutation in the set of permutations formed by the numbers in 'nums'
# Which means we need to do the following:
# 1. find the decreasing number from right to left
# 2. swap it with largest value to it's right
# 3. sort the rest to be increasing

# Approach 1: Brute force, Time: O(n!), Space: O(n)
# Approach 2: Single pass approach, Time: O(n), Space: O(1)

# Steps:
# 1. Scan from right with a loop invariant that all elements to the right of current are sorted in decreasing order
# 2. We stop when we find the property a[i - 1] < a[i] (found the first valley or decreasing number from right)
# 3. We find the element to the right of a[i - 1] that is just larger than a[i - 1] and swap a[i - 1], a[j]
# 4. We sort in dec order to the right of a[i - 1]/pivot to get the next lexicographical perm.
# 5. For decreasing order this happens to be the entire array.

# Time: O(n)
# Space: O(1)
