# @param {String[]} words
# @return {Integer[][]}
def palindrome_pairs(words)
    return [] if words.size < 2
    valid_pals, word_dict = [], {}
    words.each_with_index { |word, i| word_dict[word] = i }

    word_dict.each do |word, k|
        n = word.size()
        0.upto(n) do |j|
            prefix = word[0...j]
            suffix = word[j...n]

            # If prefix is a palindrome then reverse_suffix + prefix + suffix will be a palindrome
            if palindrome?(prefix)
                back = suffix.reverse
                if back != word && word_dict.key?(back)
                    valid_pals.push([word_dict[back], k])
                end
            end

            # If suffix is a palindrome then prefix + suffix + reverse_profix will be a palindrome
            # use the word or reverse to form palindrom only once, that's why j != n, cuz when j = 0, we wud've consider the "" and word as prefix and suffix
            if j != n && palindrome?(suffix) 
                back = prefix.reverse
                if back != word && word_dict.key?(back)
                    valid_pals.push([k, word_dict[back]])
                end
            end
        end
    end

    valid_pals
end

def palindrome?(word)
    word == word.reverse
end



# 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

# Worst case time complexity takes O(n * m * m)
# where n is the average length of the words and m is the length of wordlist.
# if the average word length is very long this solution is very slow,
# but with very long list and every word is very short this is a much better solution.
# Average case time complexity takes O(n * m).
# As in the average case, the dictionary
# (aka hashmap) takes a search of O(1) on average case time complexity.

# Time: O(n * m * m), Avg O(n * m), n - avg. word length, m - word count
# Space: O(m)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(palindrome_pairs(["a",""]), [[0,1],[1,0]])
assert_equal(palindrome_pairs(["abcd","dcba","lls","s","sssll"]), [[1, 0], [0, 1], [3, 2], [2, 4]])
assert_equal(palindrome_pairs(["bat","tab","cat"]), [[1, 0], [0, 1]])

