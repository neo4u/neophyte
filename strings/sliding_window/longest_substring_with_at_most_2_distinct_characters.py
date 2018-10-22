class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        
        Worst case time and space complexity:
        Time: O(N), Space: O(W) where N is size of string and W is size of max window
        """
        # Initialize sliding window and counts of chars in the window
        left, right = 0, 0
        counts = collections.defaultdict(int)
        
        # Slide the window down the string until we reach the end
        #
        # Loop invariant:
        # (1) The previously seen window is s[left:right]
        # (2) The right index - left index of window is always the length
        #     of the longest substring with <= 2 distinct characters
        while right < len(s):
            # Slide the right end up and update counts such that the window is now s[left:right+1]
            counts[s[right]] += 1
            right += 1
            
            # If the window has more than 2 characters, slide the left end of 
            # the window up and update counts such that the window is now s[left+1:right+1]
            if len(counts) > 2:
                counts[s[left]] -= 1
                if not counts[s[left]]:
                    del counts[s[left]]
                left += 1

        # The length of the window is the length of the longest valid substring
        return right - left

# 159. Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/