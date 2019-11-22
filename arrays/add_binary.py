class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        carry, result = 0, ''

        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            s = d1 + d2 + carry

            if s in [0, 1]:
                result = str(s) + result
                carry = 0
            elif s == 2:
                result = '0' + result
                carry = 1
            elif s == 3:
                result = '1' + result
                carry = 1
            i -= 1; j -= 1

        return result


# 67. Add Binary
# https://leetcode.com/problems/add-binary/
