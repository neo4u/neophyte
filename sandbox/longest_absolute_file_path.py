class Solution:
    def lengthLongestPath(self, string: str) -> int:
        maxlen = 0
        levels = {-1:0}

        for token in string.split('\n'):
            level = token.count('\t')
            levels[level] = levels[level - 1] + len(token) - level
            if '.' in token:
                maxlen = max(maxlen, levels[level] + level)

        return maxlen
