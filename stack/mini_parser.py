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
        raise NotImplementedError

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        raise NotImplementedError

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        raise NotImplementedError

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        raise NotImplementedError

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        raise NotImplementedError

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        raise NotImplementedError


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack, n, num = [], len(s), ''
        i = 0

        while i < n:
            c = s[i]
            if c == '[': stack.append(NestedInteger())
            elif c == ']' and len(stack) > 1:
                top = stack.pop()
                stack[-1].add(top)
            elif c.isdigit() or c == '-':
                num += c
                while i + 1 < n and s[i + 1] not in '],':
                    num += s[i + 1]
                    i += 1

                inum, num = int(num), ""
                if stack: stack[-1].add(NestedInteger(inum))
                else: stack.append(NestedInteger(inum))
            i += 1

        return stack[-1]


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        digits = "-0123456789"
        stack, num, last = [], "", None

        for c in s:
            if c in digits: num += c
            elif c == '[':
                curr = NestedInteger()
                if stack: stack[-1].add(curr)
                stack.append(curr)
            elif c in '],':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
                if c == ']': last = stack.pop()

        return last if last else NestedInteger(int(num))

# 385. Mini Parser
# https://leetcode.com/problems/mini-parser/description/


# Steps:
# 1. We use a stack and a last variable
# 2. 