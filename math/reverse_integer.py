class Solution:
    def reverse(self, x: int) -> int:
        if not x: return x
        sign = x // abs(x)                  # Capture the sign by dividing by absolute value
        x *= sign                           # Make positive if sign was negative

        reverse = 0                         # Make a var for storing reverse
        while x:
            last = x % 10                   # pop from back of x
            reverse = reverse * 10 + last   # fit into back of rev
            x //= 10                        # delete the last element

        return sign*reverse if reverse < 1<<31 else 0 # return 0 if overflow occured


# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/

# Approach 1: Pop from from back of x and push into back of reverse
# Steps
# 1. Use mod to pop from back of x
# 2. use rev * 10 + pop to add to the end of rev
# 3. div by x to remove the inserted digit
# 4. We return at the end, using bounds protection for overflow

# Time: O(log(x)), log base 10 (x) digits
# Space: O(1)

sol = Solution()
assert sol.reverse(-123) == -321
assert sol.reverse(-234342323) == -323243432
assert sol.reverse(2147483648) == 0
