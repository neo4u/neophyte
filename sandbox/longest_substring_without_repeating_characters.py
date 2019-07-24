class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_map, max_len, l, r, n = {}, 0, 0, 0, len(s)

        while r < n:
            c = s[r]
            if c in chars_map and l <= chars_map[c]:
                l = chars_map[c] + 1
            else:
                max_len = max(max_len, r - l + 1)
            chars_map[c] = r
            r += 1

        return max_len


# 'cbacdabe'

# map
# b 1
# c 3 l 1, r 3
# d 4 l 1, r 4
# l 1 r 5
# a 5
# l 3, r 5
# l 3, r 6
