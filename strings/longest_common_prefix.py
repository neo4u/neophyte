from typing import List


# Approach 2: Vertical Scanning, 2 Pass
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        shortest = min(strs, key=len)

        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] == c: continue
                return shortest[:i]

        return shortest


# Approach 4: Binary search, 2 pass with optimization
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        min_len = len(min(strs, key=len))
        l, r = 1, min_len

        while l <= r:
            mid = (l + r) // 2
            prefix = strs[0][:mid]

            if self.is_common_prefix(prefix, strs):
                l = mid + 1
            else:
                r = mid - 1

        return strs[0][:(l + r)//2]

    def is_common_prefix(self, prefix, strs):
        return all(s.startswith(prefix) for s in strs[1:])


# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

# Approach 1: Horizontal scanning

# Approach 2: Vertical Scanning, 2 Pass (OPTIMAL)

# Steps:
# - We do 1 pass of all string to find the string with the least length
# - Then we do a vertical scanning from every i from 0 to min_len - 1
#   and check if all string has same chars at i

# Time: O(prefixLength * n)
# Space: O(1)

# Approach 2: Binary Search for the prefix length

# Time: O(prefixLength * n * log(prefixLength))
# Space: O(1)

# Atleast 5 other approaches, check leetcode solutions
# Trie is another approach, but it needs more space. but time is lesser??? Not sure
