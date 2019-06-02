class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        def count(itera):
            ans = [0] * 26
            for letter in itera:
                ans[ord(letter) - ord('a')] += 1
            return ans

        def dominates(c1, c2):
            return all(x1 >= x2 for x1, x2 in zip(c1, c2))

        ans, ans_len = "", float('inf')
        target = count(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if len(word) < ans_len and dominates(count(word.lower()), target):
                ans = word
                ans_len = len(ans)

        return ans