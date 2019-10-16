from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, result = len(nums), []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue      # skip dups from left
            l, r = i + 1, n - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:   l += 1 # Move left pointer
                elif s > 0: r -= 1 # Move right pointer
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1 # Skip dups from left
                    while l < r and nums[r] == nums[r + 1]: r -= 1 # Skip dups from right

        return result


# 15. 3Sum
# https://leetcode.com/problems/3sum/description/


sol = Solution()
assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2],[ -1, 0, 1]]
