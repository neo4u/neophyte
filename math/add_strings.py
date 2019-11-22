class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        result, carry = '', 0

        while i >= 0 or j >= 0 or carry != 0:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            carry, digit = divmod(d1 + d2 + carry, 10)
            result = str(digit) + result
            i -= 1; j -= 1

        return result


# 415. Add Strings
# https://leetcode.com/problems/add-strings/description/
