from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        nums.append(upper + 1)
        prev = lower - 1

        for curr in nums:
            if curr - prev == 2:
                result.append(str(curr - 1))
            elif curr - prev > 2:
                result.append(f"{prev + 1}->{curr - 1}")
            prev = curr

        return result


# 163. Missing Ranges
# https://leetcode.com/problems/missing-ranges/description/

# sam, 123, 4
# sai, 345, 20
# ram, 456, 25
# sai, 123, 30

# def asdfasdf(log):
#     logs = log.split('\n')
#     for l in logs:
#         name, num, ts = l.split(",")






# [0 5]
# 0 + 1, 5 - 1

# [10, 15, 100]

# 16 - 99

# 1,2,3
