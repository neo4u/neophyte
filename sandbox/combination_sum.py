class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.bt(nums, 0, [], target)
        return self.result

    def bt(self, nums, s_idx, path, rem):
        if rem == 0:
            self.result.append(path.copy())
            return

        for i in range(s_idx, len(nums)):
            if rem - nums[i] < 0: continue
            self.bt(nums, i, path + [nums[i]], rem - nums[i])


# [1,2,3]  sum = 5

# [1,1,1,1,1]

# [1,2,2]
# [1,]