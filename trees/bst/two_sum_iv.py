# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.dfs(root, k, set())

    def dfs(self, node, target, visited):
        if not node:
            return False

        if target - node.val in visited:
            return True

        visited.add(node.val)
        return self.dfs(node.left, target, visited) or self.dfs(node.right, target, visited)


# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     public int val;
#  *     public TreeNode left;
#  *     public TreeNode right;
#  *     public TreeNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#     public bool FindTarget(TreeNode root, int k)
#     {
#         var set = new HashSet<int>();
#         return FindTargetR(root, set, k);
#     }

#     private bool FindTargetR(TreeNode root, HashSet<int> set, int target)
#     {
#         if (root == null) return false;

#         if (set.Contains(target - root.val)) return true;

#         set.Add(root.val);

#         return FindTargetR(root.left, set, target) || FindTargetR(root.right, set, target);
#     }
# # }

