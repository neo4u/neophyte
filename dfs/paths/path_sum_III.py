import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        self.paths, self.cache = 0, collections.defaultdict(int)
        self.cache[0] = 1
        self.dfs(root, sum, 0)
        return self.paths

    def dfs(self, node, k, cur_path_sum):
        if not node: return
        cur_path_sum += node.val

        self.paths += self.cache[cur_path_sum - k]
        self.cache[cur_path_sum] += 1

        self.dfs(node.left, sum, cur_path_sum)
        self.dfs(node.right, sum, cur_path_sum)

        self.cache[cur_path_sum] -= 1


# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/description/


# Approach 1: Double DFS

# Approach 2: Memoization

# Intuition:
# 1. This is very similar to cumulative sum problems in arrays
# 2. If (cum_sum - k) appears in the cache it means that the difference between the old sum and new sum is k

# Steps:
# 1. This 

# Time: O(n)
# Space: O(n), for cache

# https://leetcode.com/problems/path-sum-iii/discuss/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/184470
