class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]

            if top.isInteger(): return True
            else:
                self.stack.pop()
                self.stack.extend(top.getList()[::-1])
        return False


# 341. Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/description/


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# next(): Time: O(1)
# hasNext(): Time: O(n)

# Overall Space: O(n)
