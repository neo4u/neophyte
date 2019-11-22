class Solution:
    def bulbSwitch(self, n: int) -> int:
        nums = [True] * n
        for i in range(2, n + 1):
            nums[i - 1::i] = list(map(lambda x: not x, nums[i - 1::i]))

        return nums.count(True)


# 319. Bulb Switcher
# https://leetcode.com/problems/bulb-switcher/description/

# As we know that there are n bulbs, let's name them as 1, 2, 3, 4, ..., n.

# - You first turn on all the bulbs.
# - Then, you turn off every second bulb.(2, 4, 6, ...)
# - On the third round, you toggle every third bulb.(3, 6, 9, ...)
# - For the ith round, you toggle every i bulb.(i, 2i, 3i, ...)
# - For the nth round, you only toggle the last bulb.(n)
