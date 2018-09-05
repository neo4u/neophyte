# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Integer[][]}
# def path_sum(root, sum)
# 	@paths = []
# 	dfs(root, sum, [])
# 	@paths
# end

# def dfs(root, sum, visited)
# 	return if root.nil?
# 	visited << root.val

# 	if is_leaf?(root) && root.val == sum
# 		visited << root.val
# 		@paths << visited
# 	else
# 		dfs(root.left, sum - root.val, visited)
# 		dfs(root.right, sum - root.val, visited)
# 	end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Integer[][]}
def path_sum(root, sum)
	return [] if root.nil?

	@paths = []
	dfs(root, sum, [])
	@paths
end

def dfs(node, sum, visited)
	return if node.nil?

	if !node.left && !node.right && sum == node.val
		visited << node.val
		@paths.push(visited)
	else
    # we pass by value visited + [node.val] rather than by reference,
    # because we need the reference for next level of tree
    # without the previous values persisting
		dfs(node.left, sum - node.val, visited + [node.val])
		dfs(node.right, sum - node.val, visited + [node.val]) 
	end
end

