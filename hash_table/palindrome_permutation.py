import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = collections.Counter(s)
        odd_c_count = 0

        for _, count in counts.items():
            if count % 2 == 1: odd_c_count += 1
        return odd_c_count <= 1


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = collections.Counter(s)

        return len(filter(lambda x: x % 2 == 1, counts.values())) <= 1

# 266. Palindrome Permutation
# https://leetcode.com/problems/palindrome-permutation/description/
