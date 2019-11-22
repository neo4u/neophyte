
class Solution1:
    def base2(self, N: int) -> str:
        if N == 0 or N == 1: return str(N)
        return self.base2(N >> 1) + str(N & 1)

    def baseNeg2(self, N: int) -> str:
        if N == 0 or N == 1: return str(N)
        return self.baseNeg2(-(N >> 1)) + str(N & 1)


class Solution:
    def baseNeg2(self, N: int) -> str:
        result = ''

        while N:
            result = str(N & 1) + result
            N = -(N >> 1)

        return result if result else '0'

    def base2(self, N: int) -> str:
        result = ''

        while N:
            result = str(N & 1) + result
            N = N >> 1

        return result if result else '0'


# 1017. Convert to Base -2
# https://leetcode.com/problems/convert-to-base-2/description/



# Approach 1: Recursive

# Time: 
# Space: 

# Approach 2: Iterative

# Time:
# Space: 
