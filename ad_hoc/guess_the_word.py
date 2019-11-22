# LC Solution
class Solution(object):
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in zip(wordlist[i], wordlist[j]))
                   for j in range(N)] for i in range(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path=()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess


# 2nd FASTEST
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def distance(s1, s2):
            ret = 0
            for i in range(6):
                if s1[i]==s2[i]:
                    ret += 1
            return ret
        
        while len(wordlist)>0:
            nxtList = []
            idx = random.randrange(len(wordlist))
            dist = master.guess(wordlist[idx])
            for i in range(len(wordlist)):
                if i!=idx and distance(wordlist[idx], wordlist[i])==dist:
                    nxtList.append(wordlist[i])
            wordlist = nxtList




# FASTEST
import random
class Solution:
    def same_matches(self, origin, word, expected_matches):
        matches = 0
        for i in range(len(origin)):
            if origin[i] == word[i]:
                matches += 1
        return matches == expected_matches

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        random_word = wordlist[random.randint(0, len(wordlist) - 1)]
        matches = master.guess(random_word)
        if matches == 6: return

        filtered_wordlist = []
        for w in wordlist:
            if w == random_word: continue
            if self.same_matches(random_word, w, matches):
                filtered_wordlist.append(w)
        self.findSecretWord(filtered_wordlist, master)


# 843. Guess the Word
# https://leetcode.com/problems/guess-the-word/description/
