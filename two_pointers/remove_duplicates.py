from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_non_dup = 0
        n, i = len(nums), 1

        while i < n:
            if nums[i] != nums[last_non_dup]:
                last_non_dup += 1
                nums[last_non_dup] = nums[i]
            i += 1

        return last_non_dup + 1


# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# In place
# Since the array is already sorted, we can keep two pointers i and j,
# where i is the slow-runner while j is the fast-runner. As long as nums[i] = nums[j],
# we increment j to skip the duplicate.

# When we encounter nums[j] = nums[i],
# the duplicate run has ended so we must copy its value to nums[i + 1]nums[i+1].
# i is then incremented and we repeat the same process again until j reaches the end of array.
