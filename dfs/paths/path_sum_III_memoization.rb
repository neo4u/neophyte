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
	@paths, @cache = 0, {0 => 1} 
	dfs(root, sum, 0)

	@paths
end

def dfs(node, sum, cur_path_sum)
	return if !node
	cur_path_sum += node.val

	old_path_sum = cur_path_sum - sum
	
	@paths += @cache.fetch(old_path_sum, 0)
	@cache[cur_path_sum] = @cache.fetch(cur_path_sum, 0) + 1

	dfs(node.left, sum, cur_path_sum)
	dfs(node.right, sum, cur_path_sum)
	
	@cache[cur_path_sum] -= 1
end

# 2.2 Complexity analysis:
# 2.2.1 Space complexity
# O(n) extra space as we store the cache

# 2.2.1 Time complexity
# O(n) as we just traverse once