import collections
class Solution(object):
    def totalFruit(self, tree):
        fruits, l, r, n = 0, 0, 0, len(tree)
        counts = collections.Counter()

        while r < n:
            counts[tree[r]] += 1

            while len(counts) > 2:
                l_tree = tree[l]
                counts[l_tree] -= 1
                if counts[l_tree] == 0: del counts[l_tree]
                l += 1

            fruits = max(fruits, r - l + 1)
            r += 1

        return fruits



# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/description/