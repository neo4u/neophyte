from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            i = m + n - 1
            if nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]     # Copy nums1 element as it is the max element
                m -= 1                      # Move nums1's last index to left
            else:
                nums1[i] = nums2[n - 1]     # Copy nums2 element as it is the max element
                n -= 1                      # Move nums2's last index to left

        if n > 0: nums1[:n] = nums2[:n]     # If something is left from nums2 copy it over into the first n indexes of nums1
        # The check is redundant we can do the copy regardless


# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/


# Approach Merge Sort
# - Start placing elements in their final places from the back.
# - Each time we place an element from nums1's inital part to the back part
# - we're freeing a position for elements to replace the front part.
# - Any number in one being overwritten shud've already been copied over to it correct position,
#   So we're not losing any data

# Time: O(m + n), to put simply linear
# Space: O(1)

sol = Solution()
assert sol.merge([2, 0], 1, [1], 1) == [1, 2]
assert sol.merge([1, 2, 3, 4, 5], 5, [8, 9, 10, 11, 12, 12, 16], 7) == [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 12, 16]
