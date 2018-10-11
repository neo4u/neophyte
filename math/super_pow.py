# // Here we use the following two properties:
# // n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
# // If b = m*10 + d, we have a**b == (a**d)*(a**10)**m
class Solution(object):
    def superPow(self, a, b):
        if not b:
            return 1
        return pow(a, b.pop(), 1337)*self.superPow(pow(a, 10, 1337), b)%1337