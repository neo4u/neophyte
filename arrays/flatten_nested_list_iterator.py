class NestedIterator(object):
    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]
        
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


# 341. Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/