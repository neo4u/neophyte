class Solution:
    def toHex(self, num: int) -> str:
        symb = '0123456789abcdef'
        num &= 0xFFFFFFFF
        result = []

        while num:
            cur = num % 16
            result.append(symb[cur])
            num //= 16

        return ''.join(result[::-1]) if result else '0'


# 405. Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
