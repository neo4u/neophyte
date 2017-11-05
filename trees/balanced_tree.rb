module Trees
  module BalancedTree
    def self.is_balanced?(tree)
      (max_depth(tree.root) - min_depth(tree.root) <= 1)
    end

    private
    def self.max_depth(tree)
      return 0 if ((not tree.respond_to? :left) or (not tree.respond_to? :right))
      return 1 + [max_depth(tree.left), max_depth(tree.right)].max
    end

    def self.min_depth(tree)
      return 0 if ((not tree.respond_to? :left) or (not tree.respond_to? :right))
      return 1 + [min_depth(tree.left), min_depth(tree.right)].min
    end
  end
end
