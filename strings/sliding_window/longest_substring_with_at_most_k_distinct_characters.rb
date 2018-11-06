# @param {String} s
# @param {Integer} k
# @return {Integer}
def length_of_longest_substring_k_distinct(s, k)
    map = Array.new(128,0)
    # left and right bounds for window (l and r),
    # longest length of string to return as result (longets),
    # counter for number of elements in the window,
    # replace s with the an array of bytes for the characters
    l, r, longest, counter, s = 0, 0, 0, 0, s.bytes

    while r < s.size
        counter += 1 if map[s[r]] == 0
        map[s[r]] += 1
        r += 1

        while counter > k
            map[s[l]] -= 1
            counter -= 1 if map[s[l]] == 0
            l += 1
        end
        longest = [longest, r - l].max
    end

    longest
end

# 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Approach 1: Use sliding window
# 1. Fix pointers l, r to 0
# 2. Keep expanding r to next char and see if it breaks the utmost k property
# 3. If it breaks keep kicking out an instance of a char (from window)
#    and increment left pointer until at most k chars
# 4. If it doesn't break keep expanding window by incrementing right pointer
#    and incrementing map of counts for each char

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring_k_distinct('eceba', 2), 3)
assert_equal(length_of_longest_substring_k_distinct('aa', 1), 2)
assert_equal(length_of_longest_substring_k_distinct('ccaabbb', 3), 7)

