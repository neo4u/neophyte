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


# Intuition:
# 1. Finding 2's complement:
#    - Step 1: Flip all bits (1's complement)
#    - Step 2: Add 1
#    Example : Let's say you want to take 2's complement of -1 and you're only considering 8 bit numbers
#    - Step 1 can become: '1111_1111' + num = '1111_1111' - '1' = '1111_1110'
#    - Step 2: '11111110' + '1' = '11111111'
#      actually '1111_1111' = 2 ** 8 - 1
#                                                  1's complement
#                                                ------------------
#      so we can simplify step 1 and step 2 to : (2 ** 8 - 1 + num) + 1 = 2 ** 8 + num

# 2. In two's complement notation:
#    - Most negative 32 bit number is -2^(n - 1)
#    - Most positive number is 2^(n - 1) - 1
