# Segment Tree
class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])

class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hashTable)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hashTable[nums[i]] - 1))
            tree.update(hashTable[nums[i]], 1)
        return r[::-1]


# Binary Indexed Tree
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r

class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]


# Binary Search Tree
class BinarySearchTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.leftTreeSize = 0

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not root:
            self.root = BinarySearchTreeNode(val)
            return 0

        if val == root.val:
            root.count += 1
            return root.leftTreeSize

        if val < root.val:
            root.leftTreeSize += 1

            if not root.left:
                root.left = BinarySearchTreeNode(val)
                return 0
            return self.insert(val, root.left)

        if not root.right:
            root.right = BinarySearchTreeNode(val)
            return root.count + root.leftTreeSize

        return root.count + root.leftTreeSize + self.insert(
            val, root.right)

class Solution(object):
    def countSmaller(self, nums):
        tree = BinarySearchTree()
        return [
            tree.insert(nums[i], tree.root)
            for i in xrange(len(nums) - 1, -1, -1)
        ][::-1]


# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# Approach 1: Segment Tree
# Approach 2: Binary Indexed Tree
# Approach 3: Binary Search Tree
# Approach 4: Merge-sort
# MergeSort-based solution is a standard way to solve problems related to inverse numbers.

# Here is an example to illustrate the general idea of MergeSort-based algorithm:
# Now we want to consider an array
#             6 4 1 8 7 5 2 9

# First thing first, split the array into to subarrays:
#             6 4 1 8
#             7 5 2 9

# and then calculate the inverse numbers within the group:
#                   1 4(1) 6(1,4) 8
#                   2 5(2) 7(2,5) 9
# where the numbers in the parentheses are the numbers that should be counted when we calculate the inverse number.

# Now we need to merge these two arrays into one sorted array. The first element to be put into the sorted destination array is the "1" in the first array.
#  1                  4(1) 6(1,4) 8
#                   2 5(2) 7(2,5) 9               merged elements in the 2nd array = ()

# The second element to merge is the "2" in the second array:
#  1 2                4(1) 6(1,4) 8
#                     5(2) 7(2,5) 9               merged elements in the 2nd array = (2)

# The third element to merge is the "4" in the first array:
#  1 2 4(1,2)              6(1,4) 8
#                     5(2) 7(2,5) 9               merged elements in the 2nd array = (2)

# When we merge the "4(1)", we found that "4" is actually greater than all merged elements in the second array (i.e. [2]). Therefore, we also need to consider those elements. Therefore, the numbers in the parenthese of 2 become (1)+(2) = (1,2). Next step:
#  1 2 4(1,2) 5(2)         6(1,4) 8
#                          7(2,5) 9               merged elements in the 2nd array = (2,5)

# Next (add the inverse number of element "6" by 2)
#  1 2 4(1,2) 5(2) 6(1,4,2,5)     8
#                          7(2,5) 9               merged elements in the 2nd array = (2,5)

# So and so forth, finally reach
#  1 2 4(1,2) 5(2) 6(1,4,2,5) 7(2,5) 8(2,5,7) 9
#                                                 merged elements in the 2nd array = (2,5,7,9)
# Additionally, when we need to count the inverse number, we do not need to record the exact elements, we only need to record the numbers. So, we can use a variable to record the number of "merged elements in the 2nd array" (for example, semilen in the code beneath) and the number of smaller elements of each element (for example, results[idx] in the code beneath).

# Complexities:
# Time: O(n log n)
# Space: O(n)