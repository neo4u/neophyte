# @param {String} s
# @return {String}
def reverse_words(s)
    s.split.map(&:reverse).join(" ")
end

# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Complexity Analysis
# Time complexity: O(n), Just 1 loop of length of string
# Space complexity: O(1)