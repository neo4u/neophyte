from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.bt(nums, 0, [], target)
        return self.result

    def bt(self, nums, s_idx, path, rem):
        if rem == 0: return self.result.append(path)

        for i in range(s_idx, len(nums)):
            if nums[i] > rem: continue
            self.bt(nums, i, path + [nums[i]], rem - nums[i])


# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/


# Approach 1: Backtracking
# 1. We use every possible number in the array as the start of path,
#    Then we use every possible element as the second element, and third element and so on.
#    Think of picking from an unlimited bag of the numbers in the nums
# 2. So we use a s_idx to mark which index of the array we are starting our choice of next element from
# 3. We use path to keep track of elements we've encountered so far to form our current sum, in the current recursion stack
# 4. We use rem to keep track of how much of the target is remaining. This is what is left for us to form
# 5. We end our recursion once rem == 0. Because our sum has been formed, we need to save the path we took to get here
# 6. We use a pruning logic of 'if nums[i] > rem: continue' to avoid going down bath recursion paths,
#    this is because nums[i] > rem can never cause rem to become 0.

# Time: O(2 ^ n)
# Space: O(2 ^ n)

# Example 1: [2, 3, 5]
# bt(idx=0, path=[], rem=8)
#     bt(idx=0, path=[2], rem=6)
#         bt(idx=0, path=[2, 2], rem=4)
#             bt(idx=0, path=[2, 2, 2], rem=2)
#                 bt(idx=0, path=[2, 2, 2, 2], rem=0)
#                 Adding path: [2, 2, 2, 2]
#             i: 1, pruning
#             i: 2, pruning
#             bt(idx=1, path=[2, 2, 3], rem=1)
#             i: 1, pruning
#             i: 2, pruning
#         i: 2, pruning
#         bt(idx=1, path=[2, 3], rem=3)
#             bt(idx=1, path=[2, 3, 3], rem=0)
#             Adding path: [2, 3, 3]
#         i: 2, pruning
#         bt(idx=2, path=[2, 5], rem=1)
#         i: 2, pruning
#     bt(idx=1, path=[3], rem=5)
#         bt(idx=1, path=[3, 3], rem=2)
#         i: 1, pruning
#         i: 2, pruning
#         bt(idx=2, path=[3, 5], rem=0)
#         Adding path: [3, 5]
#     bt(idx=2, path=[5], rem=3)
#     i: 2, pruning

# Example 2: [2, 3, 6, 7]
# bt(idx=0, path=[], rem=7)
#     bt(idx=0, path=[2], rem=5)
#         bt(idx=0, path=[2, 2], rem=3)
#             bt(idx=0, path=[2, 2, 2], rem=1)
#             i: 0, pruning
#             i: 1, pruning
#             i: 2, pruning
#             i: 3, pruning
#             bt(idx=1, path=[2, 2, 3], rem=0)
#             Adding path: [2, 2, 3]
#         i: 2, pruning
#         i: 3, pruning
#         bt(idx=1, path=[2, 3], rem=2)
#         i: 1, pruning
#         i: 2, pruning
#         i: 3, pruning
#     i: 2, pruning
#     i: 3, pruning
#     bt(idx=1, path=[3], rem=4)
#         bt(idx=1, path=[3, 3], rem=1)
#         i: 1, pruning
#         i: 2, pruning
#         i: 3, pruning
#     i: 2, pruning
#     i: 3, pruning
#     bt(idx=2, path=[6], rem=1)
#     i: 2, pruning
#     i: 3, pruning
#     bt(idx=3, path=[7], rem=0)
#     Adding path: [7]


sol = Solution()
assert sorted(sol.combinationSum([2, 3, 6, 7], 7)) == sorted([
    [7],
    [2, 2, 3]
])
assert sorted(sol.combinationSum([2, 3, 5], 8)) == sorted([
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5]
])
