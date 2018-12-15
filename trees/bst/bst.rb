module Trees
  class BinarySearchTree
    attr_accessor :root

    class Node
      attr_reader :value
      attr_accessor :left, :right

      def initialize(value)
        @value = value
        @left = nil
        @right = nil
      end
    end

    def initialize
      @root = nil
    end

    def insert(value, node = nil)
      return @root = Node.new(value) if @root.nil?
      node = @root if node.nil?

      if value == node.value
        node
      elsif value < node.value
        node.left.nil? ? node.left = Node.new(value) : insert(value, node.left)
      elsif value > node.value
        node.right.nil? ? node.right = Node.new(value) : insert(value, node.right)
      end
    end

    def search(value, node = nil)
      return nil if @root.nil?
      node = @root if node.nil?

      if value == node.value
        node
      elsif value < node.value
        node.left.nil? ? nil : search(value, node.left)
      elsif value > node.value
        node.right.nil? ? nil : search(value, node.right)
      end
    end

    def delete_node(root, key)
      return nil if root.nil?

      if key < root.val
        root.left = delete_node(root.left, key)
      elsif key > root.val
        root.right = delete_node(root.right, key)
      else
        if root.left.nil?
          root = root.right
        elsif root.right.nil?
          root = root.left
        else
          min = find_min_node(root)
          root.val = min
          root.right = delete_node(root, min)
        end
      end

      root
    end

    def find_min_node(root)
      root = root.left while root.left
      root
    end

    def balanced?(node)
      return true if node.nil?
      (height(node.left) - height(node.right)).abs <= 1 && balanced?(node.left) && balanced?(node.right)
    end

    def height(node)
      return 0 if node.nil?
      1 + [height(node.left), height(node.right)].max
    end
  end
end
