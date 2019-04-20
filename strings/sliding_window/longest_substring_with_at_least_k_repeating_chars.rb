# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_substring(s, k)
    longest, more_than_k = 0, 0
    counts = Array.new(26, 0)
    s.each_char do |c|
        idx = c.ord - 'a'.ord
        counts[idx] += 1
        more_than_k += 1 if counts[idx] == k
    end

    1.upto(more_than_k) do |u|
        counts = Array.new(26, 0)
        l, r, uniq, k_or_more = 0,0,0,0
        while r < s.size
            if uniq <= u
                idx = s[r].ord - 'a'.ord
                uniq += 1 if counts[idx] == 0
                counts[idx] += 1
                k_or_more += 1 if counts[idx] == k
                r += 1
            else
                idx = s[l].ord - 'a'.ord
                counts[idx] -= 1
                uniq -= 1 if counts[idx] == 0
                k_or_more -= 1 if counts[idx] == k - 1
                l += 1
            end
            longest = [longest, r - l].max if uniq == u && uniq == k_or_more
        end
    end

    longest
end


# 395. Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Steps
# 1. Iterate through the possible max distinct char sizes (1 to more_than_k)
# 2. For each distinct char length u (from 1 to more_than_k)
#    we find the longest substring with at most u distinct chars like in:
#    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# 3. Use sliding window to expand r when our distinct chars count (uniq) are < u,
#    we inc l and kick out chars one by one when our uniq is > u
# 4. For each time our unique chars are all of more_than_k we capture the longest string size

# Time: O(n)
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(longest_substring('aaabb', 3), 3)
assert_equal(longest_substring('ababbc', 2), 5)
assert_equal(longest_substring('aaabbb', 3), 6)
assert_equal(longest_substring('', 1), 0)
assert_equal(longest_substring('weitong', 2), 0)
assert_equal(longest_substring('bbaaacbd', 3), 3)
