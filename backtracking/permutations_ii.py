from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.bt(nums, 0)
        return self.result

    def bt(self, nums, s_idx):
        if s_idx == len(nums) - 1: return self.result.append(nums.copy())
        used = set()

        for i in range(s_idx, len(nums)):
            if nums[i] in used: continue
            used.add(nums[i])
            if i != s_idx: nums[i], nums[s_idx] = nums[s_idx], nums[i]
            self.bt(nums, s_idx + 1)
            if i != s_idx: nums[i], nums[s_idx] = nums[s_idx], nums[i]


class Solution2:
    def permuteUnique(self, nums):
        if not nums: return []
        self.result = []
        nums.sort()
        self.bt(nums, [])
        return self.result

    def bt(self, nums, path):
        if not nums: return self.result.append(path)

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: continue
            nums_wo_curr = nums[:i] + nums[i + 1:]
            self.bt(nums_wo_curr, path + [num])


# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/description/


# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

sol = Solution()
assert sol.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

sol2 = Solution2()
assert sol2.permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
