class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x ^ y
        count = 0

        while val:
            count += val & 1
            val >>= 1

        return count
