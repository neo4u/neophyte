require_relative '../trees/traversals'


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
      expect(@bst.preorder()).to eq ['d', 'b', 'm', 'k', 'p', 't', 'c', 'a', 'g', 'f', 'h']
    end

    it 'should return values in inorder' do
      expect(@bst.inorder()).to eq ['m', 'b', 'p', 'k', 't', 'd', 'a', 'g', 'c', 'f', 'h']
    end

    it 'should return values in postorder' do
      expect(@bst.postorder()).to eq ['m', 'p', 't', 'k', 'b', 'g', 'a', 'h', 'f', 'c', 'd']
    end
  end
end
