from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n == 0: return []
        self.result = []
        nums = list(range(1, 10))
        self.bt(nums, 0, k, [], n)
        return self.result

    def bt(self, nums, s_idx, k, path, rem):
        if rem == 0 and len(path) == k: return self.result.append(path)

        for i in range(s_idx, len(nums)):
            if nums[i] > rem: continue
            self.bt(nums, i + 1, k, path + [nums[i]], rem - nums[i])


# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/


# Approach 1: Backtracking
# 1. Similar to problem Combination Sum 2.
# 2. Only difference being we also check check length of the path
# 3. The other important thing is we don't want duplicatesj, so we use i + 1
