class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth, ret = 1, 0
        while nestedList:
            ret += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
            depth += 1
        return ret

# When updating the nestedList, we won't need to check "if not x.isInteger()". It is already checked, in the "ret + = ..." statement.
# So, this works:

class Solution2(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth, ret = 1, 0
        while nestedList:
            ret += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList], []) 
            depth += 1
        return ret