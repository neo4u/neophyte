# Approach 1: Backtracking with two hashes and without starts_with
# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern_match(pattern, str)
    bt(pattern, str)
end

def bt(pattern, str, i = 0, j = 0, p_hash = {}, w_hash = {})
    return true if i == pattern.size && j == str.size
    return false if i == pattern.size || j == str.size

    p = pattern[i]
    j.upto(str.size - 1) do |k|
        w = str[j..k]
        next if (p_hash.key?(p) && p_hash[p] != w) || (w_hash.key?(w) && w_hash[w] != p)

        mapped_at_this_iter = false
        p_hash[p], w_hash[w], mapped_at_this_iter = w, p, true if !p_hash.key?(p) && !w_hash.key?(w)
        remainder = bt(pattern, str, i + 1, k + 1, p_hash, w_hash)
        return true if remainder
        if mapped_at_this_iter
            p_hash.delete(p)
            w_hash.delete(w)
        end
    end

    false
end

# pattern = "abab", str = "redblueredblue"

require 'set'

# Approach 2: Backtracking with a hash and hash set and delete after backtracking
# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern_match2(pattern, str)
    bt(pattern, str)
end

def bt(pattern, str, p_idx = 0, s_idx = 0, map = {}, words_used = Set.new)
    return s_idx == str.size if p_idx == pattern.size
    p = pattern[p_idx]
    w = map[p]

    if w
        return false if !str[s_idx...str.size].start_with?(w)
        return true if bt(pattern, str, p_idx + 1, s_idx + w.size, map, words_used) # Recursively solve sub-problem
    else
        s_idx.upto(str.size - 1) do |i|
            word = str[s_idx..i]
            next if words_used.include?(word) # is 'a' is used to match 'red' then 'b' can't be used to match red
            words_used.add(word)
            map[p] = word
            return true if bt(pattern, str, p_idx + 1, i + 1, map, words_used)
            map.delete(p)
            words_used.delete(word)

            # The above three lines can be replaced by below lines.
            # Since we're creating duplicate hashes, we don't need to to delete after bt
            # But creating duplicates is very slow, so watch out
            # return true if bt(pattern, str, p_idx + 1, i + 1, map.dup, words_used.dup)
        end
    end

    false
end

# 291. Word Pattern II
# https://leetcode.com/problems/word-pattern-ii/

# Approach 1: Backtracking

# Steps
# 1. 


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(word_pattern_match("abab", "redblueredblue"), true)
assert_equal(word_pattern_match("aaaa", "asdasdasdasd"), true)
assert_equal(word_pattern_match("aabb", "xyzabcxzyabc"), false)

assert_equal(word_pattern_match2("abab", "redblueredblue"), true)
assert_equal(word_pattern_match2("aaaa", "asdasdasdasd"), true)
assert_equal(word_pattern_match2("aabb", "xyzabcxzyabc"), false)

