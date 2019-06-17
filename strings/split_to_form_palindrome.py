class Solution:
    def split_palindrome(self, a, b):
        n = len(a)
        l, r, i = 0, n - 1, 0

        while l < r:
            if a[l] == b[r] or a[r] == a[l]: # only 2 ptrs required since the partition moves at the same speed on both str
                i += 1
            l += 1; r -= 1

        return i - l == r - i


sol = Solution()
assert sol.split_palindrome("abcbbbb", "xxxbcba")
# assert sol.split_palindrome("abcbbbb", "xxxbcba")

# Google problem
# Given 2 strings a and b with the same length.
# Strings are alligned one under the other.
# We can choose an index and split both strings into 4 subtrings: a1 + a2 and b1 + b2.
# Find out if it's possible to split a and b such that a1 + b2 or a2 + b1 forms a palindrome.

# Example 1:

# Input: a = "abcbbbb", b = "xxxbcba"
# Output: true
# Explanation:
# abc|bbbb
# xxx|bcba

# We can split the strings at index 3. We will get a1 = "abc", a2 = "bbbb" and b1 = "xxx", b2 = "bcba"
# a1 + b2 forms a palidnrome "abcbcba" so return true.

# Follow-up:
# Now it's allowed to split the strings independently:
# a|bcbbbb
# xxxbcb|a
# So in the exampe above a can be splitted into a1 = "a" a2 = "bcbbbb" and b can be splitted b1 = "xxxbcb" b2 = "a". As a result a1+ b2 forms a palindrome "aa". Find the longest palindrome.
