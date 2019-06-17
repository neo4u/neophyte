import collections

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_map, pre_sum = collections.defaultdict(int), 0
        sum_map[0] = -1
        max_len = 0

        for i, n in enumerate(nums):
            pre_sum += n
            if pre_sum - k in sum_map:
                max_len = max(max_len, i - sum_map[pre_sum - k])

            if pre_sum not in sum_map: sum_map[pre_sum] = i

        return max_len


# k = 3
# 1 1 2


# 1 2 4


# map
# 0 -1
# 1  0
# 2  1

# [-2,-1,2,1] k = 1
# map

# [1,-1,5,-2,3]  k = 3

# [1, 0,5, 3,6]

# map
# 0  -1
