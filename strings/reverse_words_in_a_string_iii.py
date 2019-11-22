class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda x : x[::-1], s.split())))


# https://leetcode.com/problems/reverse-words-in-a-string-ii/
# 186. Reverse Words in a String II

# Time: O(n)
# Space: O(n)
