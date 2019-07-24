from typing import List
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted, weighted = 0, 0
        while nestedList:
            next_level = []
            for item in nestedList:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    next_level.extend(item.getList())

            weighted += unweighted
            nestedList = next_level

        return weighted


# 364. Nested List Weight Sum II
# https://leetcode.com/problems/nested-list-weight-sum-ii/description/


# [1,[4,[6]]]

# uws = 1
# next = [4, [6, [1]]]
# w = 1

# uws = 5
# w = 6
# nextl = [6]

# uws 11
# w = 17
# next_l = [1]

# uws = 12
# w = 12 + 17