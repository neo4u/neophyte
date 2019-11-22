from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        r, w = 0, 0                                         # r is read head, w is write head

        while r < n:
            curr, count = chars[r], 0                       # Read using read head 'r'
            while r < n and curr == chars[r]:               # Read until diff char using 'r'
                count += 1; r += 1

            chars[w] = curr; w += 1                         # Write the curr char using write head 'w'
            if count == 1: continue                         # if only 1 char, then we've already written it

            for c in str(count):                            # Write the count of char using write head 'w'
                chars[w] = c; w += 1

        return w


# 443. String Compression
# https://leetcode.com/problems/string-compression/description/


# Intuition:
# We use the read and write heads for this


sol = Solution()

assert sol.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert sol.compress(["a"]) == 1
assert sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
