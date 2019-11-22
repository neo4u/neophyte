# Approach 2: Time: O(n), Space: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.is_palindrome(s): return True
        l, r = 0, len(s) - 1
        while s[l] == s[r]: l += 1; r -= 1
        # Exclude char at left or exclude char at right pointers
        return self.is_palindrome(s[l:r]) or self.is_palindrome(s[l + 1:r + 1])

    def is_palindrome(self, s):
        return s == s[::-1]


# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

# Approach 1: Brute Force [Time Limit Exceeded] Time: O(n^2), Space: O(N)

# Approach 2: Greedy [Accepted]  Time: O(n), Space: O(1)
# Solution above

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
