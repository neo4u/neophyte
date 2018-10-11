class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Calculate sign of divisor i.e., sign will be negative
        # only iff either one of them is -ve else it will be +ve
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, i = divisor, 1

            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1

        # Max of least and answer and min of max 32 int and answer,
        # as our solution is bounded by min_int and max_int
        return min(max(-2147483648, sign * quotient), 2147483647)

# Binary search like bit manipulation solution
# https://www.sigmainfy.com/blog/leetcode-divide-two-integers.html

# Efficient Approach : Use bit manipulation in order to find the quotient.

# Alright, now we get to the main part.
# We know that division is actually the backward of multiplication,
# for example , 20 / 5 = 4 can be seen as 4 * 5 = 20.

# Here what we are going to do is to find the multiplication.
# We set tmp as divisor (5) and set count to 1.
# As long as the tmp is <= dividend (20),
# we left shift << which is same as multiply 2 but without using multiplication.
