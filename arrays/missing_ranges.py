from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums.append(upper + 1)
        prev, result = lower - 1, []

        for curr in nums:
            if curr - prev == 2:
                result.append(f"{curr - 1}")
            elif curr - prev > 2:
                result.append(f"{prev + 1}->{curr - 1}")
            prev = curr

        return result


# 163. Missing Ranges
# https://leetcode.com/problems/missing-ranges/description/
