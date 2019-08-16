class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.result = float('inf')
        self.n, self.m = len(nums), m
        self.dfs(nums, 0, 0, -float('inf'), 0)
        return self.result

    def dfs(self, nums, i, count, curr_max, curr_sum):
        if i == self.n and count == self.m:
            self.result = min(self.result, curr_max)
            return
        if i == self.n: return

        if i > 0:
            curr_sum += nums[i]
            self.dfs(nums, i + 1, count, max(curr_max, curr_sum), curr_sum)

        if count < self.m:
            self.dfs(nums, i + 1, count + 1, max(curr_max, nums[i]), nums[i])


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        nlen = len(nums)
        dp = [[sys.maxint] * (m + 1) for _ in range(nlen + 1)]
        dp[0][0] = 0
        presum = [0] * (nlen + 1)
        for i, n in enumerate(nums):
            presum[i + 1] = n + presum[i]

        for i in range(1, nlen + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], presum[i] - presum[k]))

        return dp[nlen][m]

#     1 2 3 4 5 6 7 8
#   0 0 0 0 0 0 0 0 0
#   0         x 
# 1 0         x
# 2 0         x
# 3 0         x
# 4 0         x
# 5 0           o
# 6 0
# 7 0
