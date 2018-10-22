# Approach 1: No optimations, just simple sliding window.
# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)
    return "" if !s || s.empty? || !t || t.empty?

    dict_t = {}
    t.each_char do |c|
        dict_t[c] ||= 0
        dict_t[c] += 1
    end
    # required is the Number of unique characters in t, which need to be present in the desired window.
    # l, r are left and right pointer

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these
    # conditions are met.
    required, formed, l, r = dict_t.size, 0, 0, 0
    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}
    # ans tuple of the form [window length, left, right]
    ans = [Float::INFINITY, nil, nil]

    while r < s.size
        char = s[r]
        window_counts[char] = window_counts.fetch(char, 0) + 1
        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        formed += 1 if dict_t.key?(char) && window_counts[char] == dict_t[char]
        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r && formed == required
            char = s[l]
            # Save the smallest window until now.
            ans = [r - l + 1, l, r] if r - l + 1 < ans[0]
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[char] -= 1
            formed -= 1 if dict_t.key?(char) && window_counts[char] < dict_t[char]
            # Move the left pointer ahead, this would help to look for a new window.
            l += 1
        end
        # Keep expanding the window once we are done contracting.
        r += 1
    end

    ans[0] == Float::INFINITY ? "" : s[ans[1]...ans[2] + 1]
end

# Beats 50% (Leetcode optimal solution) Time and Space: O(m + n) where m, n = s.size, t.size
# We reduce the number of operations from 2 * |S| + |T| to 2 * |filtered_S| + |S| + |T|
# In cases where filtered_S <<< S, this approach helps optimize a little bit
# @param {String} s
# @param {String} t
# @return {String}
def min_window2(s, t)
    return "" if !s || s.empty? || !t || t.empty?

    dict_t = {}
    t.each_char do |c|
        dict_t[c] ||= 0
        dict_t[c] += 1
    end

    # Only contains the chars in t and corresp indices
    filtered_s = []
    s.each_char.with_index do |c, i|
        filtered_s.push([i, c]) if dict_t.key?(c)
    end

    # required is the Number of unique characters in t, which need to be present in the desired window.
    # l, r are left and right pointer

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these
    # conditions are met.
    required, formed, l, r = dict_t.size, 0, 0, 0
    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}
    # ans tuple of the form [window length, left, right],
    # loop invariant is that ans always contains [length of window, win_start, win_end]
    ans = [Float::INFINITY, nil, nil]

    while r < filtered_s.size
        char = filtered_s[r][1]
        window_counts[char] = window_counts.fetch(char, 0) + 1 # Inc count of curr char in window_counts

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        formed += 1 if dict_t.key?(char) && window_counts[char] == dict_t[char]

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r && formed == required
            char = filtered_s[l][1]

            # Save the smallest window until now.
            w_start, w_end = filtered_s[l][0], filtered_s[r][0]
            ans = [w_end - w_start + 1, w_start, w_end] if w_end - w_start + 1 < ans[0]

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[char] -= 1
            formed -= 1 if window_counts[char] < dict_t[char]

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1
        end

        # Keep expanding the window once we are done contracting.
        r += 1
    end

    ans[0] == Float::INFINITY ? "" : s[ans[1]..ans[2]]
end


# Fastest ruby submission, beats 90-100%, Time and Space: O(m + n) where m, n = s.size, t.size
# Trick is to use array instead of hash, and use each_byte instead of each char
# @param {String} s
# @param {String} t
# @return {String}
def min_window3(s, t)
    return "" if s.empty? || t.empty?

    # Because z represents int value of 122 so we need 123 elements in the array, only last 26 entries will be used.
    rem = Array.new(123, 0)
    required = t.length
    t.each_byte { |byte| rem[byte] += 1 }

    i, start, head = 0, 0, 0
    string = s
    s = s.bytes
    diff = s.size + 1

    while i < s.size
        # if(required > 0)
        rem[s[i]] -= 1
        required -= 1 if rem[s[i]] >= 0
        i += 1
        # end
        while required == 0
            # Update the new start and length of window
            if i - start < diff
                diff  = i - start
                head = start
            end

            rem[s[start]] += 1
            required += 1 if rem[s[start]] > 0
            start += 1
        end
    end

    diff == s.size + 1 ? "" : string[head...head + diff]
end


# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/

# Approach 1: Sliding Window
# The solution is pretty intuitive. We keep expanding the window by moving the right pointer.
# When the window has all the desired characters,
# we contract (if possible) and save the smallest window till now.
# Algorithm
# 1. We start with two pointers, left and right initially pointing to the first element of the string S.
# 2. We use the rightright pointer to expand the window until we get a desirable window
#    i.e. a window that contains all of the characters of T.
# 3. Once we have a window with all the characters, we can move the left pointer ahead one by one.
#    If the window is still a desirable one we keep on updating the minimum window size.
# 4. If the window is not desirable any more, we repeat step2 onwards.

# Complexity Analysis
# Time Complexity: O(|S| + |T|) where |S| and |T| represent the lengths of strings SS and T.
#                  In the worst case we might end up visiting every element of string S twice,
#                  once by left pointer and once by right pointer. |T| represents the length of string T.
# Space Complexity: O(|S| + |T|). |S| when the window size is equal to the entire string S.
#                   |T| when T has all unique characters. 

# Approach 2: Optimized Sliding Window
# Algorithm
# This kind of scenario might happen when length of string T is way too small than
# the length of string S and string S consists of numerous characters which are not present in T.
# We create a list called filtered_S which has all the characters from string S along with their indices in S,
# but these characters should be present in T.

# S = "ABCDDDDDDEEAFFBC" T = "ABC"
# filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
# Here (0, 'A') means in string S character A is at index 0.
# We can now follow our sliding window approach on the smaller string filtered_S.

# Complexity Analysis
# Time Complexity: O(|S| + |T|) where |S| and |T| represent the lengths of strings S and T.
#                  The complexity is same as the previous approach.
#                  But in certain cases where ∣filtered_S∣ <<< |S|,
#                  the complexity would reduce because the number of iterations would be 2*|filtered_S| + |S| + |T|.
# Space Complexity : O(|S| + |T|).

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(min_window('abcdab', 'abcda'), 'abcda')
assert_equal(min_window2('abcdab', 'abcda'), 'abcda')
assert_equal(min_window3('abcdab', 'abcda'), 'abcda')