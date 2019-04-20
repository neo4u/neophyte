class Master:
    def __init__(self):
        print("initialized")

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        raise NotImplementedError

# Approach 1: Simple Counting and Guessing
class Solution1:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def getMatchNum(w, p): return sum(1 for c1, c2 in zip(w, p) if c1 == c2)
        possible = {w for w in wordlist}
        while possible:
            p = possible.pop()
            match = master.guess(p)
            if match == 6: return
            possible = {w for w in possible if getMatchNum(w, p) == match}
        return

class Solution1:
    
    def findSecretWord(self, wordlist, master):
        n = 0
        while n < 6:
            guess = random.choice(wordlist)
            n = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == n]


import collections
import itertools
# Approach 2: MinMax
class Solution:
    def match(self, word1, word2): 
        count = 0
        for w1, w2 in zip(word1, word2):
            if w1 == w2: count += 1
        return count



    def print_counter(self, count):
        for key, value in count.items():
            print(key, value)

    def findSecretWord(self, wordlist, master):
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            print(count[wordlist[2]])
            guess = min(wordlist, key=lambda w: count[w])
            self.print_counter(count)
            print(guess)
            return
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]


class Solution(object):
    def match(self, a, b): return sum(i == j for i, j in zip(a,b))
    
    def findSecretWord(self, wordlist, master):
        n = 0
        while n < 6:
            histogram = {}
            
            ## build heuristic
            for w1 in wordlist:
                histogram[w1] = [0] * 7
                for w2 in wordlist:
                    histogram[w1][self.match(w1, w2)] += 1
                histogram[w1] = max(histogram[w1])
            guess = min(wordlist, key=lambda w: histogram[w])
            print(guess)
            print(histogram)
            n = master.guess(guess)
            
            ## take only those words that have same match as the guess (necessary req. to be a total match)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]



# LeetCode Solution Using MinMax
class Solution2(object):
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        self.H = [[sum(a==b for a,b in itertools.izip(wordlist[i], wordlist[j]))
                   for j in xrange(N)] for i in xrange(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in xrange(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess


# 843. Guess the Word
# https://leetcode.com/problems/guess-the-word/

# Approach 1: Simple Counting and Guessing


# Approach 2: MinMax
# Steps:
# 1. Choose a word that has closest distance to the maximum number of words in wordlist
# 2. Use that as the first guess and get the distance from secret.
# 3. We get to eliminate all the words that don't have that distance,
#    because they can't be candidates as they don't have
#    the same distance from the first guess word as secret.
# 4. We continue the loop till we get a correct guess,
#    eliminating words and choosing the closest word,
#    
# Time: O(N^2og N), where N is the number of words, and assuming their length is O(1).
#                  Each call to solve is O(N^2), and the number of calls is bounded by O(log N).
# Space: O(N^2)

sol = Solution()
master = Master()
sol.findSecretWord(["gaxckt","trlccr","jxwhkz","ycbfps","peayuf",
                    "yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia",
                    "ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl",
                    "bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg",
                    "roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm",
                    "iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl",
                    "tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed",
                    "hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls",
                    "tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw",
                    "mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr",
                    "lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr",
                    "syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv",
                    "mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph",
                    "twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu",
                    "xgqpsr","wxdyho","alrplq","brklfk"], master) 
