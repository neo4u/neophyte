class Solution(object):
    def isCompleteTree(self, root):
        nodes = [(root, 0)]
        i = 0
        while i < len(nodes): # This just means while our index is within the array
            node, v = nodes[i]
            if node:
                nodes.append((node.left, 2*v + 1))
                nodes.append((node.right, 2*v + 2))

            i += 1

        return  nodes[-1][1] == len(nodes) - 1


# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/

# Intuition
# In a complete binary tree, if we give indexes to each node, including the nulls,
# we get a complete sequence 0, 1, 2, 3, 4, .... with non-null nodes
# We in doing so we get a null node in between then it is not a complete binary tree


# Steps:
# 1. We use 'nodes' array to store tuple of (node, position)
# 2. We loop while index is less than the number of elements in 'nodes'
# 3. We assign an index using the typical heap notation, left child is 2*v+1, and rigt is 2*v+2
# 4. We exit when i has gone beyond number of items in the list
# 5. At this point, the last ID given out should be equal to number of 

# Input: [1,2,null,4,5]
#        1
#      /
#     2
#    / \
#   4   5
# Example without right sub-tree
# i = 0
# node, v = [1, 0]
# [[1, 0], [2, 1], [None, 2]]

# i = 1
# node, v = [2, 1]
# [[1, 0], [2, 1], [None, 2], [4, 3], [5, 4]]

# i = 2
# node, v = [None, 2]
# Don't add anything, 'nodes' remains same inc i
# [[1, 0], [2, 1], [None, 2], [4, 3], [5, 4]]

# i = 3
# node, v = [4, 3]
# [[1, 0], [2, 1], [None, 2], [4, 3], [5, 4], [None, 7], [None, 8]]

# i = 4
# node, v = [5, 4]
# [[1, 0], [2, 1], [None, 2], [4, 3], [5, 4], [None, 7], [None, 8], [None, 9], [None, 10]]

# i = 5
# node, v = [None, 7]

# i = 6
# node, v = [None, 8]

# i = 7
# node, v = [None, 9]

# i = 8
# node, v = [None, 10]

# len(9) - 1 = 8 = but nodes[-1][1] == 10 so not complete

# Example 2:
# Input: [1,2,3,4,5,6]
#        1
#      /   \
#     2     3
#    / \   /
#   4   5 6

# i = 0
# node, v = [1, 0]
# [[1, 0], [2, 1], [3, 2]]

# i = 1
# node, v = [2, 1]
# [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]


# i = 2
# node, v = [3, 2]
# [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [None, 6]]

# i = 3
# node, v = [4, 3]
# [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [None, 6], [None, 7], [None 8]]

# i = 4
# node, v = [5, 4]
# [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [None, 6], [None, 7], [None 8], [None, 9], [None, 10]]

# i = 5
# node, v = [6, 5]
# [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [None, 6], [None, 7], [None 8], [None, 9], [None, 10], [None, 11], [None, 12]]

# i = 6
# node, v = [None, 6]
# []

# i = 7
# node, v = [None, 9]
# []


# i = 8
# node, v = [None, 10]
# ...i = 11

# node[-][1] = 12 == len(nums) - 1 = 13 - 1 == 12
