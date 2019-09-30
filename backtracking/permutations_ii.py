from typing import List

# Approach 1: With swapping
class Solution:
    TAB = '\t'
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.bt(nums, 0)
        return self.result

    def bt(self, nums, s_idx, depth=0):
        print(f"{self.TAB * depth}bt({nums}, {s_idx + 1}")
        if s_idx == len(nums) - 1:
            print(f'{self.TAB * depth}Adding')
            return self.result.append(nums.copy())
        used = set()
        print(f'{self.TAB * depth}Used is {used}')

        for i in range(s_idx, len(nums)):
            print(f'{self.TAB * depth}i: {i}')
            if nums[i] in used:
                print(f'{self.TAB * depth}Skipping nums[i]: {nums[i]} as it is in used')
                continue

            used.add(nums[i])
            if i != s_idx: nums[i], nums[s_idx] = nums[s_idx], nums[i]
            self.bt(nums, s_idx + 1, depth + 1)
            if i != s_idx: nums[i], nums[s_idx] = nums[s_idx], nums[i]

# Approach 1: With slicing
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


# Approach 1: With Swapping
# bt([1, 1, 2], 1
# Used is {}
# i: 0
#     bt([1, 1, 2], 2
#     Used {}
#     i: 1
#         bt([1, 1, 2], 3
#         Adding [1 1 2]
#     i: 2
#         bt([1, 2, 1], 3
#         Adding [1 2 1]
# i: 1
# Skipping nums[i]: 1 as it is in used
# i: 2
#     bt([2, 1, 1], 2
#     Used is {}
#     i: 1
#         bt([2, 1, 1], 3
#         Adding [2 1 1]
#     i: 2
#     Skipping nums[i]: 1 as it is in used

# Approach 2: With Splicing


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
