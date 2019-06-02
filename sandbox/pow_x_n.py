class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1

        if n < 0:
            x = 1 / x
            n = -n

        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


# Input: a = 2, b = [3,1,0]
# 2**(0*10**order) * 2**(1*10**1) * 2**(3**10**2)
# 1 0

# order = 0

# 2 * (n - 1 - order) * 10** order * 2 * 10**(n - 1 - order + 1)

# 2 ^ 20 = (2 ^2) ^ 10