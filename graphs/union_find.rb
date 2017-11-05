# make_set(x) initializes disjoint set for object x
# find(x) returns representative object of the set containing x
# union(x,y) makes two sets containing x and y respectively into one set

# Applications:
#   - Kruskal's algorithm for finding minimal spanning trees
#   - Finding connected components in graphs
#   - Finding connected components in images (binary)
#   - Find cycles in a graph (Valid Tree)

# def make_set(x)
#   x.parent = x
#   x.rank   = 0
# end

# def find(x)
#   x.parent == x ? x : find(x.parent)
# end

# def union(x, y)
#   x_root = find(x)
#   y_root = find(y)
#   if x_root.rank > y_root.rank
#     y_root.parent = x_root
#   elsif x_root.rank < y_root.rank
#     x_root.parent = y_root
#   elsif x_root != y_root # Unless x and y are already in same set, merge them
#     y_root.parent = x_root
#     x_root.rank += 1
#   end
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


# require 'test/unit'
# extend Test::Unit::Assertions
# l = "abcdefg".each_char.map { |c| Node.new(c) }

# l.each { |node| make_set(node) }

# sets = l.map { |x| find(x).to_s }
# puts "set representatives:\t#{sets}"
# set_count = sets.group_by { |v| v }.size
# puts "number of disjoint sets:\t#{set_count}"

# assert_not_equal(find(l[0]), find(l[2]))
# union(l[0], l[2])                    # joining first and third
# assert_equal(find(l[0]), find(l[2]))

# assert_not_equal(find(l[0]), find(l[1]))
# assert_not_equal(find(l[2]), find(l[1]))
# union(l[0], l[1])                    # joining first and second
# assert_equal(find(l[0]), find(l[1]))
# assert_equal(find(l[2]), find(l[1]))

# union(l[-2], l[-1])                  # joining last two sets
# union(l[-3], l[-1])                  # joining last two sets

# sets = l.map { |x| find(x).to_s }
# puts "set representatives:\t#{sets}"
# set_count = sets.group_by { |v| v }.size
# puts "number of disjoint sets:\t#{set_count}"
