from typing import List


class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        self.find_median(nums, 0, n - 1)
        half = (n + 1) // 2

        nums[::2] = nums[:half][::-1]
        nums[1::2] = nums[half:][::-1]

    def find_median(self, nums, l, r):
        i = j = k = l + 1
        mid = len(nums) // 2
        sentinel = nums[l]

        while k <= r:
            if nums[k] < sentinel:
                nums[k], nums[j] = nums[j], nums[k]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1; j += 1; k += 1
            elif nums[k] > sentinel:
                k += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1; k += 1

        nums[l], nums[i - 1] = nums[i - 1], nums[l]

        if i - 1 <= mid < j: return nums[mid]

        if mid >= j:    return self.find_median(nums, j, r)
        else:           return self.find_median(nums, l, i - 2)


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


# 324. Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/description/


# Intuition:
# This is a good article that breaks down the algorithm nicely,
# https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof?page=2

# I put the smaller half of the numbers on the even indexes and
# the larger half on the odd indexes, both from right to left:

# Example nums = [1,2,...,7]      Example nums = [1,2,...,8]

# Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
# Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
# --------------------------      --------------------------
# Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5

# Approach 1: Sort and distribute into indexes
# Steps:
# 1. Sort the numbers
# 2. Divide the sorted array into 2 equal or unequal part such that first part is larger if !=
# 3. Distribute the reversed 1st half into the even indexes
# 4. Distribute the reversed 2nd half into the odd indexes
# 5. If a solution exists, it should be found using the above method

# Time: O(n * log(n))
# Space: O(1)

# Approach 2: Use median
# Steps:
# - Find the median and then use (len + 1) / 2 to split into two parts
# - Less than median to the left and greater than median to the right
# - Once it's split using quickselect or 3-way partitioning
# - Do the distribution in a similar way as the previous approach

# Time: O(n) Avg Time, O(n ^ 2) Worst Time,
# Space: O(1), ?? What about recursion depth? So I don't know for sure about this.
