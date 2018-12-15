module Trees
  class BST
    attr_accessor :root

    class Node
      attr_accessor :value, :left, :right

      def initialize(value, left = nil, right = nil)
        @value = value
        @left = left
        @right = right
      end
    end

    def initialize(root)
      @root = root
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

    def delete_node(root, key)
      return nil if root.nil?

      if key < root.val
        root.left = delete_node(root.left, key)
      elsif key < root.val
        root.right = delete_node(root.right, key)
      else
        if root.left.nil?
          root = root.right
        elsif root.right.nil?
          root = root.left
        else
          min = min_val_node(root)
          root.val = min
          root.right = delete_node(root.right, min)
        end
      end
    end

    def min_val_node(root)
      root = root.left while root.left
    end
  end
end