class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        ranger = 1
        while (x // ranger) >= 10: ranger *= 10

        while x:
            l, r = x // ranger, x % 10      # l for digit from left and r for digit from right
            if l != r: return False         # Return if unequal
            x = (x % ranger) // 10          # Mod ranger removes first digit, div 10 remove last digit
            ranger //= 100                  # remove 10 for removal of digit at each end

        return True


# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/


# Example: x = 5115

# ranger = 1, x // ranger = 5115 // 1 = 5115
# ranger = 10,  x // ranger = 5115 // 10 = 511
# ranger = 100, x // ranger = 5115 // 100 = 51
# ranger = 1000, x // ranger = 5115 // 1000 = 5, we break cuz x // ranger == 5115 // 1000 == 5 < 10

# Now, we compare first and last digits and keep reducing the number from front and back
# l, r = 5115 // 1000, 5115 % 1000 == 5, 5 and 5 == 5 so we get 5115 % 1000 == 115, then we // 10 == 115 // 10 == 11
# Again compare last and first
# return True

sol = Solution()

assert sol.isPalindrome(100001) == True
assert sol.isPalindrome(123321) == True
assert sol.isPalindrome(1221) == True
