import collections


class Solution:
    def lengthLongestPath(self, string: str) -> int:
        maxlen = 0
        levels = collections.defaultdict(int)

        for token in string.split('\n'):
            level = token.count('\t')
            token_len = len(token) - level
            levels[level] = levels[level - 1] + token_len

            if '.' in token:
                maxlen = max(maxlen, levels[level] + level)

        return maxlen


# 388. Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/description/