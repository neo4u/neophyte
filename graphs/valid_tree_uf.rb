# # @param {Integer} n
# # @param {Integer[][]} edges
# # @return {Boolean}
# def valid_tree(n, edges)
#   return false if edges.size != n - 1

#   def find(x)
#     x.parent == x ? x : find(x.parent)
#   end

#   def union(x, y)
#     i, j = find(x), find(y)
#     if i.rank > j.rank
#       j.parent = i
#     elsif i.rank < j.rank
#       i.parent = j
#     elsif i != j  # This means same rank so if they're not from same set (i == j) merge them
#       j.parent = i
#       i.rank += 1
#     end
#     i != j        # If this is false it means there is a cycle. Think Why? [edge between already connected nodes]
#   end

#   def make_set(label)
#     x = Node.new(label)
#     x.parent, x.rank = x, 0
#     x
#   end

#   set = {}
#   0.upto(n - 1) { |node| set[node] = make_set(node) }

#   edges.map { |edge| union(set[edge[0]], set[edge[1]]) }.all?
# end

# class Node
#   attr_accessor :parent, :rank
#   def initialize(label)
#     @label = label
#   end

#   def to_s
#     @label
#   end
# end

# n, edges = 6, [[0, 1], [0, 2], [2, 5], [3, 4], [3, 5]]
# # n, edges = 5, [[0,1],[0,2],[2,3],[2,4]]
# p valid_tree(n, edges)
