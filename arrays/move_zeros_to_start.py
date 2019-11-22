from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        lzi = n

        for i in range(n - 1, -1, -1):
            if nums[i] == 0: continue
            lzi -= 1
            nums[lzi], nums[i] = nums[i], nums[lzi]

        print(nums)
        return nums

sol = Solution()
assert sol.moveZeroes([1, 0, 2, 0, 3]) == [0, 0, 1, 2, 3]
