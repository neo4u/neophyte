from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        curr = 0

        while curr <= r:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                curr += 1; l += 1
            elif nums[curr] == 2:
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
            else:
                curr += 1


# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/description/


# Intuition:
# - We use the below 3-way partitioning technique
# - l reprents the index to the left of which are all the 0s
# - r reprents the index to the right of which are all the 1s
# - curr points to the start of the unknowns, everything between curr and r are unknowns
# - everything between l and curr are 1s, bcuz they're to the right of l so not 1s and to the left of curr so not unknown

# Time: O(n)
# Space: O(1)


#   0          1       uk       2
# ---------  --------        ---------
# 0          l       i       r        n
