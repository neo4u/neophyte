import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        win_map = collections.defaultdict(int)
        l, r = 0, 0
        max_len = 0

        while r < n:
            in_c = s[r]
            win_map[in_c] += 1

            while len(win_map) > k:
                out_c = s[l]
                win_map[out_c] -= 1
                if win_map[out_c] == 0: win_map.pop(out_c)
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len



# 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Approach 1: Use sliding window
# 0. We maintain:
#    - map:     Array of counts and
#    - uniq: counts of distinct chars in the current window
# 1. Fix pointers l, r to 0
# 2. Keep expanding r to next char and see if it breaks the utmost k property
# 3. If it breaks keep kicking out a char (from sliding window)
#    and increment left pointer until at most k chars
# 4. If it doesn't break keep expanding window by incrementing right pointer
#    and incrementing map of counts for each char

# Time: O(n)
# Space: O(1)


sol = Solution()
assert sol.lengthOfLongestSubstringKDistinct('eceba', 2) == 3
assert sol.lengthOfLongestSubstringKDistinct('aa', 1) == 2
assert sol.lengthOfLongestSubstringKDistinct('ccaabbb', 3) == 7
