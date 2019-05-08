# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    map = {}
    l, longest = 0, 0

    s.each_char.with_index do |c, r|
        # puts "c: #{c}"
        if map.key?(c) && map[c] >= l
            l = map[c] + 1
            # puts "contracting window: l: #{l}"
        else
            # puts "capturing window: l: #{l}"
            longest = [longest, r - l + 1].max
        end
        map[c] = r
        # puts "map: #{map} | longest: #{longest}"
    end

    longest
end


# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Examples: 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Sample output from logged code
# c: a
# capturing window: l: 0
# map: {"a"=>0} | longest: 1
# c: b
# capturing window: l: 0
# map: {"a"=>0, "b"=>1} | longest: 2
# c: c
# capturing window: l: 0
# map: {"a"=>0, "b"=>1, "c"=>2} | longest: 3
# c: a
# contracting window: l: 1
# map: {"a"=>3, "b"=>1, "c"=>2} | longest: 3
# c: b
# contracting window: l: 2
# map: {"a"=>3, "b"=>4, "c"=>2} | longest: 3
# c: c
# contracting window: l: 3
# map: {"a"=>3, "b"=>4, "c"=>5} | longest: 3
# c: b
# contracting window: l: 5
# map: {"a"=>3, "b"=>6, "c"=>5} | longest: 3
# c: b
# contracting window: l: 7
# map: {"a"=>3, "b"=>7, "c"=>5} | longest: 3

# Time: O(n)
# Space: O(n)


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(length_of_longest_substring("abcabcbb"), 3)
assert_equal(length_of_longest_substring("bbbbb"), 1)
assert_equal(length_of_longest_substring("pwwkew"), 3)
