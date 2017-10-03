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

    def preorder(node)
      result = []
      result << @root.value # start at root and add it's value
      result << preorder_subtree(node.root.left) # traverse left sub-tree
      result << preorder_subtree(node.root.right) # traverse right sub-tree
      p result
      result.flatten
    end

    private
    def preorder_subtree(node, result = [])
      result << node.value
      preorder_subtree(node.left, result) if node.left != nil
      preorder_subtree(node.right, result) if node.right != nil
      result
    end
  end
end

describe Trees::BinaryTree do
  before :each do
    @bst = Trees::BinaryTree.new('d') # set root

    # Left Subtree
    @bst.root.insert_left('b')
    @bst.root.left.insert_left('m')
    @bst.root.left.insert_right('k')
    @bst.root.left.right.insert_left('p')
    @bst.root.left.right.insert_right('t')

    # Right Subtree
    @bst.root.insert_right('c')

    @bst.root.right.insert_left('a')
    @bst.root.right.left.insert_right('g')

    @bst.root.right.insert_right('f')
    @bst.root.right.right.insert_right('h')

  end
  context 'traverse tree in specific order' do
    it 'should return values in preorder' do
      expect(@bst.preorder(@bst)).to eq ['d', 'b', 'm', 'k', 'p', 't', 'c', 'a', 'g', 'f', 'h']
    end
  end
end