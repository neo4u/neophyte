import collections
import json

class SolutionNKlogK(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

# Time: O(NKlogK), where N is the length of strs,
#                  and K is the maximum length of a string in strs.
#                  The outer loop has complexity O(N) as we iterate through each string.
#                  Then, we sort each string in O(KlogK) time.
# Space: O(NK)O(NK), the total information content stored in ans.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        
        for s in strs:
            chars = [0] * 26
            for c in s: chars[ord(c) - ord('a')] += 1
            result[tuple(chars)].append(s)

        return result.values()



# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/


# Time: O(NK), where N is the length of strs,
#                  and K is the maximum length of a string in strs.
#                  Counting each string is linear in the size of the string,
#                  and we count every string.
# Space: O(NK), the total information content stored in ans.

# Essentially both are O(n)

sol = Solution()
assert sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']
]
