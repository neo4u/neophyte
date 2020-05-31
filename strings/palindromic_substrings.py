class Solution:
    def countSubstrings(self, s: str) -> int:
        result, n = 0, len(s)

        for i in range(n):
            result += self.pals_from_center(s, i, i) + self.pals_from_center(s, i, i + 1)
        return result

    def pals_from_center(self, s, l, r):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
            count += 1

        return count


# https://leetcode.com/problems/palindromic-substrings/description/
# 647. Palindromic Substrings


# Approach 1: O(n**2) Time,  O(1) Space
# Total of 2n - 1 centers
# abba 4 centers at abba (n chars are n centers)
# | | | |
# a b b a
# abba has 3 center in between characters (n chars have n - 1 centers in betwee then)
# a|b|b|a
# For each center we find the number of palindromes around it.
# O(n**2) Because of the two levels of nested loops.

# Approach 2: O(n) Time, O(n) space
# O(n) Manacher's Algorithm uses an array to store palindromes as each enter
# Uses the concept of not having to check all the centers and mirroring of centers for a palindrome

# assert_equal(count_substrings('aaa'), 6)
# assert_equal(count_substrings('aaaaa'), 15)
