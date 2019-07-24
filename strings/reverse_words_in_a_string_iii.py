class Solution(object):
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        new_str = ""
        for w in s.split(" "):
            new_str += w[::-1] + " "

        return new_str.rstrip()


# Python usage seems way faster.
class Solution2(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]

# 186. Reverse Words in a String II
# https://leetcode.com/problems/reverse-words-in-a-string-ii/

# Time: O(n)
# Space: O(n)