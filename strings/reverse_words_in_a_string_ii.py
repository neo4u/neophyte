from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        self.reverse(s, 0, len(s) - 1)
        self.reverse_words(s)

    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1; r -= 1

    def reverse_words(self, arr):
        n = len(arr)
        l, r = 0, 0
        while r < n:
            while r < n and not arr[r].isspace(): r += 1
            self.reverse(arr, l, r - 1)
            r += 1; l = r

# Python usage seems way faster.
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s[:] = str(''.join(s)).split(' ')
        s[:] = reversed(s)
        s[:] = list(' '.join(s))

# 186. Reverse Words in a String II
# https://leetcode.com/problems/reverse-words-in-a-string-ii/

# Its 3n which is O(n). Here's the break down.

# 1. reverse the whole string, this is n steps.
# 2. advance fast pointer to find end of word,
#    the fast pointer just advances through whole string and never backtracks,
#    so this is n iterations.
# 3. reverse the word found, if word is length m,
#    this is m steps, but consider all words together will be n,
#    so this is also n steps total for all words.
# total is 3n which is just O(n).

# Time: O(n)
# Space: O(1)
