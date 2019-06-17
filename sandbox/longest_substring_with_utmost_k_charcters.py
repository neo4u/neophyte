import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r, count_map, max_len = 0, 0, collections.Counter(), 0

        while r < len(s):
            c = s[r]
            count_map[c] += 1

            while len(count_map) > k:
                count_map[s[l]] -= 1
                if count_map[s[l]] == 0:
                    del count_map[s[l]]
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
