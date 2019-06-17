class Solution:
    def findAndReplacePattern(self, words, pattern):
        result = []

        for word in words:
            w_hash, p_hash = {}, {}
            if len(word) != len(pattern): continue

            for i in range(len(word)):
                w_c, p_c = word[i], pattern[i]
                if (p_c in p_hash and p_hash[p_c] != w_c) or (w_c in w_hash and w_hash[w_c] != p_c): break
                p_hash[p_c] = w_c
                w_hash[w_c] = p_c
            else:
                result.append(word)
        return result
