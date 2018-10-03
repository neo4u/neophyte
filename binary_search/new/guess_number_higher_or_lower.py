# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low < high:
            mid = (low + high)//2
            res =  guess(mid)
            if res == 0 :
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1

        return l

# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

# Complexity Analysis
# Time complexity: O(logn), Binary Search is used.
# Space complexity: O(1)O(1), No extra space is used.

# We can apply Binary Search to find the given number.
# We start with the mid number. We pass that number to the guessguess function.
# If it returns a -1, it implies that the guessed number is larger than the required one.
# Thus, we use Binary Search for numbers lower than itself.
# Similarly, if it returns a 1, we use Binary Search for numbers higher than itself.
