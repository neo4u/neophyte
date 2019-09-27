class Solution(object):
    def superPow(self, a, b):
        if not b: return 1
        return pow(a, b.pop(), 1337)*self.superPow(pow(a, 10, 1337), b)%1337

# // Here we use the following two properties:
# // n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
# // If b = m*10 + d, we have a**b == (a**d)*(a**10)**m

# DIFFERENT PROBLEM SUPER POW
# Input: a = 2, b = [3,1,0]
# 2**(0*10**order) * 2**(1*10**1) * 2**(3**10**2)
# 1 0

# order = 0
# 2 * (n - 1 - order) * 10** order * 2 * 10**(n - 1 - order + 1)
# 2 ^ 20 = (2 ^2) ^ 10
