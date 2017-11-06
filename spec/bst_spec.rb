require_relative '../trees/bst'

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

describe Trees::BinarySearchTree do
  before :each do
    @bst = Trees::BinarySearchTree.new
  end

  context 'During initialization' do
    it 'should initialize with a nil root value' do
      expect(@bst.root).to eq nil
    end
  end

  context 'Interface' do
    it 'should allow a new value to be inserted as a node' do
      @bst.insert(15)
      @bst.insert(10)
      bottom_left_of_root = @bst.root.left
      expect(bottom_left_of_root.value).to eq 10
      expect(bottom_left_of_root.left).to be nil
      expect(bottom_left_of_root.right).to be nil
    end

    it 'should add values less than parent to the left as nodes' do
      @bst.insert(15)
      @bst.insert(10)
      bottom_left_of_root = @bst.root.left
      expect(bottom_left_of_root.value).to eq 10
      expect(bottom_left_of_root.left).to be nil
      expect(bottom_left_of_root.right).to be nil
    end

    it 'should add values greater than parent to the right as nodes' do
      @bst.insert(15)
      @bst.insert(20)
      bottom_right_of_root = @bst.root.right
      expect(bottom_right_of_root.value).to eq 20
      expect(bottom_right_of_root.left).to be nil
      expect(bottom_right_of_root.right).to be nil
    end
  end

  context 'Inserting' do
    it 'should assign first value to root, if root is nil' do
      @bst.insert(1)
      expect(@bst.root.value).to eq 1
    end

    it 'should build a binary search tree' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.root.left.left.value).to eq 8
      expect(@bst.root.left.right.value).to eq 12
      expect(@bst.root.right.left.value).to eq 17
      expect(@bst.root.right.right.value).to eq 25
    end

    # it 'should build a binary search tree' do
    #   @bst.insert(50) # root
    #   @bst.insert(40) # left
    #   @bst.insert(39) # left of 40
    #   @bst.insert(41) # right of 40
    #   @bst.insert(60) # right
    #   @bst.insert(59) # left of 60
    #   @bst.insert(61) # right of 60
    #   expect(@bst.root.left.left.value).to eq 8
    #   expect(@bst.root.left.right.value).to eq 12
    #   expect(@bst.root.right.left.value).to eq 17
    #   expect(@bst.root.right.right.value).to eq 25
    # end

    it 'should build a binary search tree' do
      @bst.insert(50) # root
      @bst.insert(60) # right
      @bst.insert(12) # left
      @bst.insert(40) # right
      @bst.insert(13) # left
      @bst.insert(44) # right
      @bst.insert(55) # right
      @bst.insert(46)
      expect(@bst.root.value).to eq 50
      expect(@bst.root.left.right.right.value).to eq 44
      expect(@bst.root.left.right.value).to eq 40
      expect(@bst.root.right.left.value).to eq 55
      expect(@bst.root.right.right).to eq nil
    end
  end

  context 'Search' do
    it 'should traverse the tree and find a matching leaf on the right' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.search(17).value).to eq 17
    end

    it 'should traverse the tree and find a matching leaf on the left' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.search(12).value).to eq 12
    end

    it 'should traverse the tree and find the root node if it is the search value' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.search(15).value).to eq 15
    end
  end

  context 'is the tree balanced' do
    it 'should return true if tree is empty' do
      expect(@bst.balanced?(@bst.root)).to be true
    end

    it 'should validate if tree is balanced' do
      bst_balanced = build_balanced_tree
      expect(bst_balanced.balanced?(bst_balanced.root)).to be true
    end

    it 'should validate if the tree is unbalanced' do
      bst_unbalanced = build_unbalanced_tree
      expect(bst_unbalanced.balanced?(bst_unbalanced.root)).to be false
    end
  end
end

