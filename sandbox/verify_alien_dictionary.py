from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, c in enumerate(order): order_map[c] = i

        for i in range(len(words) - 1): # -1 so that i + 1 stays in range
            w1, w2 = words[i], words[i + 1]
            m, n = len(w1), len(w2)
            min_len = min(m, n)

            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 == c2: continue
                if order_map[c1] > order_map[c2]: return False
                break
            else:
                if m > n: return False

        return True


# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

# Intuition
# - 1st word in 2 consecutive sorted words will have the smaller char at the 1st char mismatch
# - Sorted words have smaller len word first and longer word second
