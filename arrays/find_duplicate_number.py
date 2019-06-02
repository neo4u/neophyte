from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                return abs(n)
            else:
                nums[i] = -nums[i]

        return -1

sol = Solution()
assert sol.findDuplicate([1,3,4,2,2]) == 2
assert sol.findDuplicate([3,1,3,4,2]) == 3

# 287. Find the Duplicate Number

