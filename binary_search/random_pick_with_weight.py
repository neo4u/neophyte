from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.n = len(w)
        for i in range(1, self.n): w[i] += w[i - 1]
        self.weights = w
        self.cum_sum = self.weights[-1]

    def pickIndex(self) -> int:
        seed = random.randint(1, self.cum_sum)

        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if seed <= self.weights[mid]:   r = mid
            else:                           l = mid + 1

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# 528. Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/description/


# Intuition:
# - Now each time pickIndex is called, we've to return an index, 
#   with a condition that we've to return indexes in proportion to their weight
# - Simply, if w = [1, 99], pickIndex() should return 1 for 99% and 0 for 1%.
# - Similar to Lottery scheduling
# - say we have w = [1, 5, 2], easiest solution is to construct the following array
#           [1  5  5  5  5  5  2  2]
#   arr[] = [0, 1, 1, 1, 1, 1, 2, 2], then generate a random number between [0-7] and return the arr[rnd].
#   This solution is not really good due to the space requirements it has (imagine a number beeing 2 billion).
# - The optimal solution is similar but instead we construct the cumulative sum array,
#   for w = [1, 5, 2], cum_sum = [1, 6, 8]
#   Now, when pickIndex() is called we generate a random interger in the interval [1-8]
#   and when we binary search for it in [0, n], we get:
#   - all numbers <= 1 yield index 0
#   - all numbers > 1 and <= 6 yield index 1
#   - all numbers  than 6 and up to 8 are index 2. After we generate a random number to find which index to return we use binary search.



# Approach 1: Cumulative Sum + Binary Search
# Steps:
# 1. Calc cumulative sum, such that w[i] will have sum of weights upto i
# 2. Now, we pick a random integer between [1, sum_of_weights]
# 3. We binary search for that left most integer 
