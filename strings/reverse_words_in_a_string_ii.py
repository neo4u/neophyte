# Little slow but makes sense in an interview
class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """

        N = len(str)
        self.reverse(0, N-1, str)                   # Reverse the whole string
        slow, fast = 0, 0

        while fast < N:
            while fast < N and str[fast] != " ":    # This while goes within a word
                fast += 1
            # This part execution as soon as we find a space,
            self.reverse(slow, fast - 1, str)       # We reverse the part of word till before the space (i - 1)
            slow = fast + 1                         # We set slow pointer to the part after the space
            fast = slow                             # We set fast to the same point
            # We cud've done something like this: slow = fast = fast + 1

    def reverse(self, i, j, str):
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1

# Python usage seems way faster.
class Solution2(object):
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        s[:] = str(''.join(s[:])).split(' ')
        s[:] = s[::-1]
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
