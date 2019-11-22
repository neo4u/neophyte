from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_nz_idx, n = 0, len(nums)

        for i in range(n):
            if nums[i] == 0: continue
            nums[last_nz_idx], nums[i] = nums[i], nums[last_nz_idx]
            last_nz_idx += 1
