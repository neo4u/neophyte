

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        shortest = min(strs, key=len)

        for i, c in enumerate(shortest): # O(pl)
            for other in strs:           # O(n)
                if other[i] == c: continue
                return shortest[:i]


        return shortest

# Time: O(prefixLen * n)
