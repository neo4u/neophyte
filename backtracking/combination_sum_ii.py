from typing import List


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.bt(nums, 0, [], target)
        return self.result

    def bt(self, nums, s_idx, path, rem):
        if rem == 0: return self.result.append(path)

        for i in range(s_idx, len(nums)):
            if i > s_idx and nums[i] == nums[i - 1]: continue
            if nums[i] > rem: break
            self.bt(nums, i + 1, path + [nums[i]], rem - nums[i])



class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        nums.sort()
        self.bt(nums, 0, [], target)
        return self.result

    def bt(self, nums, s_idx, path, rem):
        if rem == 0: return self.result.append(path)

        used = set()
        for i in range(s_idx, len(nums)):
            if nums[i] > rem: continue
            if nums[i] in used: continue
            used.add(nums[i])
            self.bt(nums, i + 1, path + [nums[i]], rem - nums[i])



# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/


# Approach 1: Backtracking
# 1. Combination Sum I allowed duplicates. To avoid those, in the recursive call, use i + 1,
#    in order to start from the next element
# 3. Now other duplicates are also possible. Imagine [1,2,5, 7, 1] and target as 8.
#    If we use DFS we will get [1,7] and then [7,1]. How do we avoid this?
# 4. Sort candidates: [1,1,2,5,7]. Now when you start with index 0,
#    your first element will be 1. It will allow you to pick the second element as 1 too.
#    You will be able to pick [1,7]. But during recursion, when you reach the next start index as 1,
#    your recursion tree will again start from 1. This will lead to a duplicate [1,7].
#    You want to avoid this.


# Another Implementation
# class Solution:
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         all_solns = []
#         self.helper([], 0, sorted(candidates), target, all_solns)
#         return all_solns

#     def helper(self, so_far, k, nums, target, all_solns):
#         sum_so_far = sum(so_far)
#         if sum_so_far == target:
#             all_solns.append([x for x in so_far])
#         else:
#             for i in range(k, len(nums)):
#                 if i > k and nums[i] == nums[i-1]: continue
#                 if (sum_so_far + nums[i] <= target):
#                     so_far.append(nums[i])
#                     self.helper(so_far, i+1, nums, target, all_solns)
#                     so_far.pop()
#         return
