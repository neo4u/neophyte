# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[][]}
def level_order(root)
    return [] if !root
    q = []
    q.push(root)
    result = []

    while !q.empty?
        level_size = q.size
        level_vals = []

        # Exhaust all nodes appended for the current level
        level_size.times do |i|
            node = q.shift
            q.push(node.left) if node.left
            q.push(node.right) if node.right
            level_vals << node.val
        end
        result.push(level_vals)
    end
    
    result
end