from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0 or n == 0: return []
        self.result = []
        nums = list(range(1, 10))
        self.bt(nums, k, 0, [], n)
        return self.result

    def bt(self, nums, k, s_idx, path, rem):
        if rem == 0 and len(path) == k: return self.result.append(path)

        for i in range(s_idx, len(nums)):
            if nums[i] > rem: continue
            self.bt(nums, k, i + 1, path + [nums[i]], rem - nums[i])


# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/


# Approach 1: Backtracking
# 1. Similar to problem Combination Sum 1.
# 2. Only difference being we also check length of the path
# 3. The other important thing is we can't same number again,
#    so we use i + 1, as the index passed to the next level
