class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        m, n = len(words1), len(words2)
        if m != n: return False
        pair_set = set([tuple(pair) for pair in pairs])
        for i in range(m):
            a, b = words1[i], words2[i]
            if a == b: continue
            if (a, b) not in pair_set and (b,a) not in pair_set: return False

        return True