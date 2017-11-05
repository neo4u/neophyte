module Trees
  class BinarySearchTree
    attr_reader :root

    class Node
      attr_reader :parent, :left, :right

      def initialize(value)
        @parent = value
        @left = nil
        @right = nil
      end

      def insert(value)
        if value <= @parent
          @left.nil? ? @left = Node.new(value) : @left.insert(value)
        elsif value > @parent
          @right.nil? ? @right = Node.new(value) : @right.insert(value)
        end
      end
    end

    def initialize
      @root = nil
    end

    def insert(value)
      if @root.nil?
        @root = Node.new(value)
      else
        @root.insert(value)
      end
    end

    def search(value, node=@root)
      return nil if node.nil?
      if value < node.parent
        search(value, node.left)
      elsif value > node.parent
        search(value, node.right)
      else
        return node
      end
    end
  end
end
