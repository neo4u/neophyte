from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tsum = sum(A)
        if tsum % 3 != 0: return False
        if not A: return True
        expected, total, count = tsum // 3, 0, 0

        for num in A:
            total += num
            if expected == total:
                count += 1
                total = 0

        return count == 3



# 1013. Partition Array Into Three Parts With Equal Sum
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
