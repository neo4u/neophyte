import collections

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum, sum_map = 0, collections.defaultdict(int)
        sum_map[0] = -1

        for i, n in enumerate(nums):
            pre_sum += n
            if k != 0: pre_sum %= k

            if pre_sum in sum_map:
                j = sum_map[pre_sum]
                if i - j >= 2:
                    return True

            if pre_sum not in sum_map:
                sum_map[pre_sum] = i

        return False
