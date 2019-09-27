class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: x, n = 1 / x, -n

        half = self.myPow(x, n // 2)
        half_x_half = half * half

        if n % 2 == 0:  return half_x_half
        else:           return half_x_half * x


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        m, result = abs(n), 1.0

        while m:
            if m & 1: result *= x   # same as checking if odd
            x *= x
            m >>= 1                 # same as doing //= 2

        return 1 / result if n < 0 else result

class Solution3:
    def myPow(self, x: float, n: int) -> float:
        m, ans = abs(n), 1.0

        while m:
            if m % 2 == 1: ans *= x
            x *= x
            m //= 2

        return 1 / ans if n < 0 else ans



# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

# Approach 1: Brute-Force, O(n) multiply one by one

# Approach 2: Fast Power Algorithm Recursive
# Time: O(log(n)). Each time we apply the formula (x ^ n) ^ 2 = x ^ (2∗n), n is reduced by half.
#       Thus we need at most O(log(n)) computations to get the result.
# Space: O(log(n)). For each computation, we need to store the result of x^n/2.
#        We need to do the computation for O(log(n)) times, so the space complexity is O(log(n)).

# x^n = x^(n/2) * x^(n/2) * optionally x
# special, negative, x=0, n=0

# Approach 3: Fast Power Algorithm Iterative
# Time: O(log(n))
# Space: O(1)
