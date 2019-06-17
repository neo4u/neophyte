class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        if k <= 1:
            return 0
        l, r, win_prod, count = 0, 0, 1, 0

        while r < len(nums):
            win_prod *= nums[r]

            while win_prod >= k:
                win_prod //= nums[l]
                l += 1

            count += r - l + 1 # This counts every subarray with nums[l:r] formed by kicking 1 element from left as 1 more subarray with prod < k
            r += 1

        return count

# 1,2,3,4
# 2,3,4
# 3,4
# 4


# TLE 
class Solution2(object):
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        if k <= 1: return 0
        l, r, win_prod, count = 0, 0, 1, 0

        while r < len(nums):
            win_prod *= nums[r]

            while win_prod >= k:
                win_prod //= nums[l]
                l += 1

            tmp_l, tmp_win_prod = l, win_prod
            while tmp_l <= r and tmp_win_prod < k:
                count += 1
                tmp_win_prod //= nums[tmp_l]
                tmp_l += 1
            r += 1

        return count



# [1 2 3 5 100] k =40
# l 0 r 0
# c 1
# l 0, r 1
# c 3
# l 0, r 2
# c 6
# l 0, r 3
# c 10
# l 0, r 4