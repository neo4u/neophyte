# # @param {String} s
# # @return {Integer}
# def length_of_longest_substring_two_distinct(s)
#     return 0 if !s || s.empty?      # Corner case
#     return s.size if s.size <= 2    # Trivial case

#     map = Array.new(128, 0)         # O(1)
#     # left and right:   bounds for window (l and r),
#     # longest:          length of string to return as result (longest),
#     # counter:          var for number of elements in the window,
#     # replace s with the an array of bytes for the chars which contains
#     l, r, longest, counter = 0, 0, 0, 0
#     s = s.bytes

#     while r < s.size
#         counter += 1 if map[s[r]] == 0  # Inc counter if the char at r has not been seen before
#         map[s[r]] += 1                  # Update the no. of times it was seen.
#         r += 1                          # Extend window to right

#         while counter > 2                   # while chars are > 2
#             map[s[l]] -= 1                  # kick out a char and reduce its count in map 
#             counter -= 1 if map[s[l]] == 0  # If all instances of char are kicked out, then reduce counter
#             l += 1                          # reduce window from left
#         end
#         longest = [longest, r - l].max      # Keep checking the current window size to maintain a maximum
#     end

#     longest                                 # Return max window size
# end


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s: return 0
        if len(s) <= 2: return len(s)

        _map = collections.defaultdict(int)
        l, r, longest, distinct, n = 0, 0, 0, 0, len(s)

        while r < n:
            in_c = s[r]
            if _map[in_c] == 0: distinct += 1
            _map[in_c] += 1
            r += 1

            while distinct > 2:
                out_c = s[l]
                _map[out_c] -= 1                        # kick out a char and reduce its count in map 
                if _map[out_c] == 0: distinct -= 1   # If all instances of char are kicked out, then reduce counter
                l += 1                              # reduce window from left
            longest = max(longest, r - l)           # Keep checking the current window size to maintain a maximum

        return longest

# 159. Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

# Approach 1: Use sliding window
# 1. Fix pointers l, r to 0
# 2. Keep expanding r to next char and see if it breaks the utmost 2 chars property
# 3. If it breaks keep kicking out an instance of a char (from window)
#    and increment left pointer until at most 2 chars
# 4. If it doesn't break keep expanding window by incrementing right pointer
#    and incrementing map of counts for each char

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring_two_distinct('eceba'), 3)
assert_equal(length_of_longest_substring_two_distinct('ccaabbb'), 5)
