
class Solution1:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum([int(x)**2 for x in str(n)])

        return n == 1


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sum_digit_squares(n)
        fast = self.sum_digit_squares(slow)

        while fast != 1:
            if slow == fast:
                return False
            else:
                slow, fast = self.sum_digit_squares(slow), self.sum_digit_squares(self.sum_digit_squares(fast))
        return True

    def sum_digit_squares(self, n):
        # the below code is equivalent to: return sum([int(x)**2 for x in str(n)])
        result = 0

        while n:
            result += pow(n % 10, 2)
            n = n // 10

        return result


# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/
