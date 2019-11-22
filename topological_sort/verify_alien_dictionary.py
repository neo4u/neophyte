from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i, c in enumerate(order): order_map[c] = i

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            m, n = len(w1), len(w2)
            min_len, found = min(m, n), False

            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 == c2: continue
                found = True
                if order_map[c1] > order_map[c2]: return False
                break

            if m > n and not found: return False

        return True


# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/


# Steps:
# 1. Capture indices of the order string in a dictionary
# 2. Compare every two consecutive words using the steps below
#     - In every 2 words check for the smaller one and compare chars upto the min len
#     - At the first mismatch return false if w1's char appears after the w2's char
#     - We use the found variable to check if the loop exited due to finding mismatch or due to min len
#     - If mismatch is found, we break cuz any of the following characters don't mean anything,
#       as sorting is done based on the first mismatch
#     - If we exited cuz of min len and we find that w1 has greater len that means we have a case like
#       "apple" < "app" which is bad orering
# 3. Return true if false wasn't returned at every consecutive two word comparison

# Time: O(M * N) M words, N is average len of each word
# Space: O(1)
