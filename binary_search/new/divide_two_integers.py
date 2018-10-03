# Several of the most voted solutions have O((logN)^2) time complexity.
# Here I provide a faster (O(logN)) solution with the cost of O(logN) space.
# The idea is to store all the left shifted divisors that are less than the dividend in a list (array).

def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647 #python 3 have removed this constant
        MIN_INT = -2147483648
        if (divisor == 0) or (divisor == -1 and dividend == MIN_INT):
            return MAX_INT #two possible cases of overflow
        vals = []
        if ((dividend > 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0)):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            vals.append(divisor)
            divisor += divisor
        result = 0
        for i in range(len(vals) - 1, -1, -1):
            if dividend >= vals[i]:
                dividend -= vals[i]
                result += 2**i
        return result * sign

# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/