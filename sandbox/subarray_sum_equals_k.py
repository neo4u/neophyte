import collections

class Solution:
    def subarraySum(self, nums, k) :
        sum_map, pre_sum = collections.defaultdict(int), 0
        sum_map[0] = 1
        result = 0

        for n in nums:
            pre_sum += n
            result += sum_map[pre_sum - k]
            sum_map[pre_sum] += 1

        return result