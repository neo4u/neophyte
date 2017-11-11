# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

class BSTIterator
  # @param {TreeNode} root
  def initialize(root)
    @stack = []
    init_stack(root)
  end

  def init_stack(root)
    while root
      @stack << root
      root = root.left
    end
  end

  # @return {Boolean}
  def has_next()
    !@stack.empty?
  end

  # @return {Integer}
  def next()
    node = @stack.pop
    x = node.right
    while x
      @stack << x
      x = x.left
    end
    node.val
  end
end

# Your BSTIterator will be called like this:
# i, v = BSTIterator.new(root), []
# while i.has_next()
#    v << i.next
# end
