# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    used = {}
    max_len, start = 0, 0

    s.each_char.with_index do |c, i|
        if used.key?(c) && used[c] >= start
            start = used[c] + 1                     # reset window start
        else
            max_len = [max_len, i - start + 1].max  # Extend window
        end

        used[c] = i
    end

    max_len
end

# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# n is size of string, m is size of charset.
# Time complexity: O(n). Index j will iterate n times.
# Space complexity: O(min(m, n))

# Approach
# The naive approach is very straightforward. But it is too slow. So how can we optimize it?
# In the naive approaches, we repeatedly check a substring to see if it has duplicate character.
# But it is unnecessary. If a substring s[i,j] from index ii to j - 1 is already checked to have no duplicate characters.
# We only need to check if s[j]s[j] is already in the substring s[i, j].

# To check if a character is already in the substring, we can scan the substring, which leads to an O(n^2) algorithm. But we can do better.
# By using HashSet as a sliding window, checking if a character in the current substring can be done in O(1).
# A sliding window is an abstract concept commonly used in array/string problems.
# A window is a range of elements in the array/string which usually defined by the start and end indices,
# i.e. [i, j) (left-closed, right-open). A sliding window is a window that "slides" its two boundaries to the certain direction.
# For example, if we slide [i, j) to the right by 1 element, then it becomes [i+1, j+1)(left-closed, right-open).
# Back to our problem. We use HashSet to store the characters in current window [i, j)(j = i initially).
# Then we slide the index j to the right. If it is not in the HashSet,
# we slide j further. Doing so until s[j] is already in the HashSet. At this point,
# we found the maximum size of substrings without duplicate characters start with index i.
# If we do this for all i, we get our answer.

# The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps.
# Instead of using a set to tell if a character exists or not,
# we could define a mapping of the characters to its index.
# Then we can skip the characters immediately when we found a repeated character.
# The reason is that if s[j] have a duplicate in the range [i, j) with index j',
# we don't need to increase i little by little.
# We can skip all the elements in the range [i, j'] and let i to be j′+ 1 directly.

# Time: O(n)
# Space: O(min(m, n))

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring("abcabcbb"), 3)
assert_equal(length_of_longest_substring("bbbbb"), 1)
assert_equal(length_of_longest_substring("pwwkew"), 3)


# Brute force method just for learning purposes. DON'T PROPOSE THIS IN INTERVIEW :P 
# @param {String} s
# @return {Integer}
def length_of_longest_substring_brute(s)
    max, n = 0, s.size
    0.upto(n - 1) do |i|
        i.upto(n - 1) do |j|
            substr = s[i..j]
            max = substr.size if all_uniq?(substr) && substr.size > max
        end
    end

    max
end

def all_uniq?(s)
  s.chars.uniq.length == s.chars.length
end

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring_brute("abcabcbb"), 3)
assert_equal(length_of_longest_substring_brute("bbbbb"), 1)
assert_equal(length_of_longest_substring_brute("pwwkew"), 3)
