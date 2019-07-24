/* 
// * Definition for a binary tree node.
using System;

public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
} */

public class Solution
{
    public bool IsSubtree(TreeNode s, TreeNode t)
    {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;

        return AreEqual(s, t) || IsSubtree(s.left, t) || IsSubtree(s.right, t);
    }

    private bool AreEqual(TreeNode s, TreeNode t)
    {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;

        if (s.val != t.val) return false;

        return AreEqual(s.left, t.left) && AreEqual(s.right, t.right);
    }
}