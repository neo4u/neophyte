from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        result, counts = 0, [0] * 32

        for num in nums:
            i = 0

            while num:
                counts[i] += num & 1
                num >>= 1
                i += 1

        for k in counts:
            result += k * (n - k)

        return result

# Steps:
# 1. We iterate through the numbers and for each number
# 2. We iterate through each bit position, we add 1 to count[bit_position] if it has 1, else we add 0
# 3. In this way we get the counts array representing each bit position
#    and the count of number that have that bit position as 1
# 3. The we iterate through the counts array and we calculate (kC1) * ((n - k)C1) => k * (n - k)
#    which is the number of 2-size combinations of elements such that we select 1 element each from 2 differents sets.
#    1 set representing numbers that have 1s in current bit position,
#    and another representing 0 in curr bit position

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        xmap = map(lambda x: f"{x:32b}", nums)
        total, n = 0, len(nums)

        for i in zip(*xmap):
            k = i.count('1')
            total += k * (n - k)

        return total

# How k * (n - k)???
# ----------------------
# k!              (n-k)!
# ----         * ------
# (k - 1)!  * 1!    (n - k - 1) !

# => k * (n - k)