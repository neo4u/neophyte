require_relative '../trees/trees'

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
      expect(bottom_left_of_root.parent).to eq 10
      expect(bottom_left_of_root.left).to be nil
      expect(bottom_left_of_root.right).to be nil
    end

    it 'should add values less than parent to the left as nodes' do
      @bst.insert(15)
      @bst.insert(10)
      bottom_left_of_root = @bst.root.left
      expect(bottom_left_of_root.parent).to eq 10
      expect(bottom_left_of_root.left).to be nil
      expect(bottom_left_of_root.right).to be nil
    end

    it 'should add values greater than parent to the right as nodes' do
      @bst.insert(15)
      @bst.insert(20)
      bottom_right_of_root = @bst.root.right
      expect(bottom_right_of_root.parent).to eq 20
      expect(bottom_right_of_root.left).to be nil
      expect(bottom_right_of_root.right).to be nil
    end
  end

  context 'Inserting' do
    it 'should assign first value to root, if root is nil' do
      @bst.insert(1)
      expect(@bst.root.parent).to eq 1
    end

    it 'should build a binary search tree' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.root.left.left.parent).to eq 8
      expect(@bst.root.left.right.parent).to eq 12
      expect(@bst.root.right.left.parent).to eq 17
      expect(@bst.root.right.right.parent).to eq 25
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
      expect(@bst.search(17).parent).to eq 17
    end

    it 'should traverse the tree and find a matching leaf on the left' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.search(12).parent).to eq 12
    end

    it 'should traverse the tree and find the root node if it is the search value' do
      @bst.insert(15)
      @bst.insert(10)
      @bst.insert(8)
      @bst.insert(12)
      @bst.insert(20)
      @bst.insert(17)
      @bst.insert(25)
      expect(@bst.search(15).parent).to eq 15
    end
  end
end
