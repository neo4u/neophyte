from typing import List

class Master:
    def guess(self, word: str) -> int:
        pass

# Approach 2: heuristic 1
import collections
import itertools
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master'):
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: count[w])
            self.print_counter(count)
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]

    def print_counter(self, count):
        for key, value in count.items():
            print(key, value)

    def match(self, word1, word2):
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 == c2: count += 1
        return count

# Approach 2: heuristic 2

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master'):
        while wordlist:
            s = self.most_overlap_word(wordlist)     # guess the word that overlaps with most others
            n = master.guess(s)
            if n == 6: return
            # wordlist = [w for w in wordlist if self.pair_matches(s, w) == n]   # filter words with same matches
            wordlist = list(filter(lambda w: self.pair_matches(s, w) == n, wordlist))

    def pair_matches(self, a, b):                   # count the number of matching characters
        return sum(c1 == c2 for c1, c2 in zip(a, b))

    def most_overlap_word(self, candidates):
        counts = [collections.defaultdict(int) for _ in range(6)]

        for word in candidates:
            for i, c in enumerate(word):
                counts[i][c] += 1

        return max(candidates, key=lambda w: sum(counts[i][c] for i, c in enumerate(w)))


# 843. Guess the Word
# https://leetcode.com/problems/guess-the-word/

# Approach 1: Simple Counting and Guessing


# Approach 2: MinMax with heuristic
# heuristic 1: Least match
# heuristic 2: most overlap

# Steps:
# 1. Choose a word that has most overlap [highest matches with hig]
# 2. Use that as the first guess and get the distance from secret.
# 3. We get to eliminate all the words that don't have that distance,
#    because they can't be candidates as they don't have
#    the same distance from the first guess word as secret.
# 4. We continue the loop till we get a correct guess,
#    filtering words that are the at the distance of the bad guesss
#    and choosing the next most overlap word

# Time: O(n)
# Space: O(1), re-use wordList
