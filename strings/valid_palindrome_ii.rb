# Approach 2: Time: O(n), Space: O(1)
# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
    return true if palindrome?(s)
    l, r = 0, s.size - 1

    while s[l] == s[r]
        l += 1; r -=1
    end
    # Exclude char at left or exclude char at right pointers
    palindrome?(s[l...r]) || palindrome?(s[l + 1...r + 1])
end

def palindrome?(s)
    s == s.reverse
end

# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

# Approach #1: Brute Force [Time Limit Exceeded] Time: O(n^2), Space: O(N)
# class Solution(object):
#     def validPalindrome(self, s):
#         for i in xrange(len(s)):
#             t = s[:i] + s[i+1:]
#             if t == t[::-1]: return True

#         return s == s[::-1]

# Approach #2: Greedy [Accepted]  Time: O(n), Space: O(1)
# Solution above

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.