class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = str(num)
        n, digits = len(str_num), list(map(int, str_num))
        buckets = {}
        for i, x in enumerate(digits):
            buckets[x] = i

        for i in range(n):
            for k in range(9, digits[i], -1):
                if k not in buckets or buckets[k] <= i: continue
                digits[i], digits[buckets[k]] = digits[buckets[k]], digits[i]
                return int(''.join(map(str, digits)))

        return num


# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap/description/
