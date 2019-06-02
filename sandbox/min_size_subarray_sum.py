class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        min_len, cur_sum = n + 1, 0

        while r < n:
            cur_sum += nums[r]

            while cur_sum >= s:
                min_len = min(min_len, r - l + 1)

                cur_sum -= nums[l]
                l += 1
            r += 1

        return 0 if min_len == n + 1 else min_len

