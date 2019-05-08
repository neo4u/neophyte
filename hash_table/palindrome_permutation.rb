# @param {String} s
# @return {Boolean}
def can_permute_palindrome(s)
    map, count = Hash.new { |h, k| h[k] = 0 }, 0

    s.each_char { |c| map[c] += 1 }
    map.values.each { |v| count += 1 if v % 2 == 1 }

    count <= 1
end


# 266. Palindrome Permutation
# https://leetcode.com/problems/palindrome-permutation/description/


# Key Insight
# Only 1 char in a palindrom can have an odd count

