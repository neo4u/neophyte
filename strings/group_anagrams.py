import collections
import json

class SolutionNKlogK(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

# Time Complexity: O(NKlogK), where N is the length of strs,
#                  and K is the maximum length of a string in strs.
#                  The outer loop has complexity O(N) as we iterate through each string.
#                  Then, we sort each string in O(KlogK) time.
# Space Complexity: O(NK)O(NK), the total information content stored in ans.

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())


# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Complexity Analysis
# Time Complexity: O(NK), where N is the length of strs,
#                  and K is the maximum length of a string in strs.
#                  Counting each string is linear in the size of the string,
#                  and we count every string.
# Space Complexity: O(NK), the total information content stored in ans.

# Essentially both are O(n)

sol = Solution()
assert sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']
]
