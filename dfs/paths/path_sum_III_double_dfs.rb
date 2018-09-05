# Definition for a binary tree node.
# class TreeNode
#	 attr_accessor :val, :left, :right
#	 def initialize(val)
#		 @val = val
#		 @left, @right = nil, nil
#	 end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Integer}
def path_sum(root, sum)
	return 0 if !root
	@paths, @nodes = 0, []
	dfs(root)

	@nodes.each do |node|
		dfs_sum(node, sum)
	end

	@paths
end

def dfs(node)
	return if !node
	
	dfs(node.left)
	@nodes << node
	dfs(node.right)
end

def dfs_sum(node, sum)
	return if !node
	@paths += 1 if node.val == sum

	dfs_sum(node.left, sum - node.val)
	dfs_sum(node.right, sum - node.val)
end

# 1.2 Complexity analysis
# 1.2.1 Space
# Space complexity is O(1), due to there is no extra cache. However, for any recursive question, we need to think about stack overflow, namely the recursion should not go too deep.
# Assume we have n TreeNodes in total, the tree height will vary from O(n) (single sided tree) to O(logn)(balanced tree).
# The two DFS will go as deep as the tree height.
# 1.2.2 Time
# Time complexity depends on the two DFS.
# 1st layer DFS will always take O(n), due to here we will take each node out, there are in total n TreeNodes
# 2nd layer DFS will take range from O(n) (single sided tree) to O(logn)(balanced tree). This is due to here we are get all the paths from a given node. The length of path is proportional to the tree height.
# Therefore, the total time complexity is O(nlogn) to O(n^2).