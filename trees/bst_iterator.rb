# Definition for a binary tree node.
# class TreeNode
#	 attr_accessor :val, :left, :right
#	 def initialize(val)
#		 @val = val
#		 @left, @right = nil, nil
#	 end
# end

class BSTIterator
	# @param {TreeNode} root
	def initialize(root)
		@list = inorder(root)
	end

	# @return {Boolean}
	def has_next
		@list.size > 0
	end

	# @return {Integer}
	def next
		@list.shift
	end

	private
	def inorder(root, visited = [])
		return visited if root.nil?
		inorder(root.left, visited)
		visited << root.val
		inorder(root.right, visited)
	
	visited
	end
end

# Your BSTIterator will be called like this:
# i, v = BSTIterator.new(root), []
# while i.has_next()
#	v << i.next
# end