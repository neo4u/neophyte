from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, n = 1, len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            carry, digits[i] = divmod(digits[i] + carry, 10)

        if carry:   return [1] + digits
        else:       return digits


# 66. Plus One
# https://leetcode.com/problems/plus-one/description/

# 1. Use a carry, that starts out as 1
# 2. Keep adding the carry and digit at current index
# 3. After exhausting all the digits, check if carry and
#    append it from the front of list


sol = Solution()
assert sol.plusOne([0]) == [1]
assert sol.plusOne([9]) == [1, 0]
