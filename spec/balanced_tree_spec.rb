require_relative '../trees/balanced_tree'
require_relative '../trees/trees'

def build_balanced_tree
  bst = Trees::BinarySearchTree.new
  bst.insert(50) # root
  bst.insert(40) # left
  bst.insert(39) # left of 40
  bst.insert(41) # right of 40
  bst.insert(60) # right
  bst.insert(59) # left of 60
  bst.insert(61) # right of 60

  bst
end

def build_unbalanced_tree
  bst = Trees::BinarySearchTree.new
  bst.insert(50) # root
  bst.insert(60) # right
  bst.insert(12) # left
  bst.insert(40) # right
  bst.insert(13) # left
  bst.insert(44) # right
  bst.insert(55) # right

  bst
end

# -- snip snip from Cracking the Coding Interview **great book**
# The idea is very simple: the difference of min depth and max depth 
# should not exceed 1, since the difference of the min and the max depth 
# is the maximum distance difference possible in the tree.
describe Trees::BalancedTree do
  before :each do
    @bst_balanced = build_balanced_tree
    @bst_unbalanced = build_unbalanced_tree
    @bst = Trees::BinarySearchTree.new
  end

  context 'is the tree balanced' do
    it 'should return true if tree is empty' do
      expect(Trees::BalancedTree.is_balanced?(@bst)).to be true
    end

    it 'should validate if tree is balanced' do
      expect(Trees::BalancedTree.is_balanced?(@bst_balanced)).to be true
    end

    it 'should validate if the tree is unbalanced' do
      expect(Trees::BalancedTree.is_balanced?(@bst_unbalanced)).to be false
    end
  end
end
