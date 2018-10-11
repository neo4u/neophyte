class Solution:
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []

        for word, k in words.iteritems():
            n = len(word)

            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]

                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])

                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals


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
