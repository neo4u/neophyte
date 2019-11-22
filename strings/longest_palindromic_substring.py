class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, n = "", len(s)

        for i in range(n):
            longest = max(
                self.get_longest_from_center(s, i, i),
                self.get_longest_from_center(s, i, i + 1),
                longest,
                key=len
            )

        return longest

    def get_longest_from_center(self, s, l, r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1; r += 1

        return s[l + 1:r] # index l + 1 upto r - 1


# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/


# a b a
# l   r
# 1   1
# 0   2
# -1  3

# a a b b a c
# l  r 
# 2  3
# 1  4
# 0  5

# r - 1 
# - l + 1
# r - 1 - l - 1 + 1
# r - l - 1

#  i   j  => j-i+1

#  (r-1) - (l+1) + 1

#  r-1-l-1+1
#  r-2-l+1
#  r-l-1
