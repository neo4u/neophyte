from typing import List
import collections


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pre_sum, sum_map = 0, collections.defaultdict(int)
        sum_map[0] = 1
        result = 0

        for n in A:
            pre_sum += n
            if K != 0: pre_sum %= K

            if pre_sum in sum_map: result += sum_map[pre_sum]
            sum_map[pre_sum] += 1

        return result


# 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

# Similar to LC 523
