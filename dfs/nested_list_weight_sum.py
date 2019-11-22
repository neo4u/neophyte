from typing import List


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.dfs(nestedList, 1)

    def dfs(self, n_list, depth):
        d_sum = 0
        for item in n_list:
            if item.isInteger():
                d_sum += item.getInteger() * depth
            else:
                d_sum += self.dfs(item.getList(), depth + 1)

        return d_sum


class Solution2:
    def depthSum(self, nestedList: List['NestedInteger']) -> int:
        if not nestedList: return 0

        stack = [(ni, 1) for ni in nestedList]
        n_sum = 0

        while stack:
            ni, w = stack.pop()
            if ni.isInteger():
                n_sum += ni.getInteger() * w
            else:
                stack += [(nxt, w + 1) for nxt in ni.getList()]

        return n_sum


# 339. Nested List Weight Sum
# https://leetcode.com/problems/nested-list-weight-sum/description/
