class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x ^ y
        count = 0

        while val:
            count += val & 1
            val >>= 1

        return count


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/description/
