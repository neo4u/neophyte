Dir['graphs/*.rb'].each do |file|
  require_relative File.join('../', File.dirname(file), File.basename(file, File.extname(file)))
end

require 'support/graphs_helpers'


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