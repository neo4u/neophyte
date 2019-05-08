# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

# Steps:
# 1. Push process root, push left, right to stack.
# 2. So that way right is popped first and processed first and put into the level
# 3. ||= node.val takes care of setting only once.

def right_side_view(root)
    max_level, stack, right_most_at_level = -1, [[root, 0]], {}

    while !stack.empty?
        node, level = stack.pop()
        next if !node # Skip to next node if node is nil

        max_level = level if level > max_level
        right_most_at_level[level] ||= node.val # Only add value if level is not present in hash

        stack.push([node.left, level + 1])
        stack.push([node.right, level + 1]) # last in, will be first out
    end

    0.upto(max_level).map { |l| right_most_at_level[l] }
end

# Steps:
# 1. Push process root, process right and then left using dfs.
# 2. Once right is processed then we never set the node for that level again.
# 3. ||= node.val takes care of setting only once.

def right_side_view(root)
    return [] if !root
    @right_most_at_level = {}
    @max_level = -1
    dfs(root, 0)

    0.upto(@max_level).map { |l| @right_most_at_level[l] }
end

def dfs(node, level)
    @max_level = level if level > @max_level
    @right_most_at_level[level] ||= node.val
    dfs(node.right, level + 1) if node.right
    dfs(node.left, level + 1) if node.left
end

# Steps
# 1. Push right and then left into queue,
# 2. We then process right first for a given left and then never reset that value
def right_side_view(root)
    max_level, q, right_most_at_level = -1, [[root, 0]], {}

    while !q.empty?
        node, level = q.shift()
        next if !node # Skip to next node if node is nil

        max_level = level if level > max_level
        right_most_at_level[level] ||= node.val # keep only the first one existing

        q.push([node.right, level + 1]) # First in will be first out, so push right first
        q.push([node.left, level + 1])
    end

    0.upto(max_level).map { |l| right_most_at_level[l] }
end

# Subtle changes
def right_side_view(root)
    return [] if !root
    max_level, q, right_most_at_level = -1, [[root, 0]], {}
    
    while !q.empty?
        node, level = q.shift()

        max_level = level if level > max_level
        right_most_at_level[level] ||= node.val

        q.push([node.right, level + 1]) if node.right
        q.push([node.left, level + 1]) if node.left
    end
    
    0.upto(max_level).map { |l| right_most_at_level[l] }
end

# Approach 1: DFS Recursive, Time: O(n), Space: O(n)
# Approach 2: DFS Iterative, Time: O(n), Space: O(n)
# Approach 2: BFS, Time: O(n), Space: O(n)

# Keep track of right most node at every level
# For DFS we push right child last so it is the first one out
# For BFS we push right child first so it is the first one out