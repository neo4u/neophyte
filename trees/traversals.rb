module Trees
  class BinaryTree
    attr_reader :root

    class Node
      attr_reader :value, :left, :right

      def initialize(value)
        @value = value
        @left = nil
        @right = nil
      end

      def insert_left(value)
        @left = Node.new(value)
      end

      def insert_right(value)
        @right = Node.new(value)
      end
    end

    def initialize(root_value)
      @root = Node.new(root_value)
    end

    def preorder(node = nil)
      node = @root if node.nil?
      result = []
      result << node.value                                        # start at root and add it's value
      result.concat(preorder(node.left)) unless node.left.nil?    # traverse left sub-tree
      result.concat(preorder(node.right)) unless node.right.nil?  # traverse right sub-tree
      result
    end

    def inorder(node = nil)
      node = @root if node.nil?
      result = []
      result.concat(inorder(node.left)) unless node.left.nil?   # traverse left sub-tree
      result << node.value                                      # start at root and add it's value
      result.concat(inorder(node.right)) unless node.right.nil? # traverse right sub-tree
      result
    end

    def postorder(node = nil)
      node = @root if node.nil?
      result = []
      result.concat(postorder(node.left)) unless node.left.nil?   # traverse left sub-tree
      result.concat(postorder(node.right)) unless node.right.nil? # traverse right sub-tree
      result << node.value                                        # start at root and add it's value
      result
    end
  end
end
