# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def right_side_view(root)
    max_level, stack, right_most_at_level = -1, [[root, 0]], {}

    while !stack.empty?
        node, level = stack.pop()
        next if !node # Skip to next node if node is nil

        max_level = [max_level, level].max
        right_most_at_level[level] ||= node.val # Only add value if level is not present in hash

        stack.push([node.left, level + 1])
        stack.push([node.right, level + 1]) # last in, will be first out
    end

    0.upto(max_level).map { |l| right_most_at_level[l] }
end

# @param {TreeNode} root
# @return {Integer[]}
def right_side_view(root)
    max_level, q, right_most_at_level = -1, [[root, 0]], {}

    while !q.empty?
        node, level = q.shift()
        p level
        next if !node # Skip to next node if node is nil

        max_level = [max_level, level].max
        right_most_at_level[level] ||= node.val # keep only the first one existing

        q.push([node.right, level + 1]) # First in will be first out, so push right first
        q.push([node.left, level + 1])
    end

    0.upto(max_level).map { |l| right_most_at_level[l] }
end

# Approach 1: DFS, Time: O(n), Space: O(n)
# Approach 2: BFS, Time: O(n), Space: O(n)

# Keep track of right most node at every level
# For DFS we push right sub-tree last so it is the first one out
# For BFS we push right sub-tree first so it is the first one out