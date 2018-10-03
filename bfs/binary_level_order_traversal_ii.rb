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
def zigzag_level_order(root)
    return [] if !root
    q, result = [[root, 0]], []
    
    while !q.empty?
        level_vals, n = [], q.size
        n.times do |i|
            node, level = q.shift
            if level.even?
                level_vals.push(node.val)
            else
                level_vals.unshift(node.val)
            end

            q.push([node.left, level + 1]) if node.left
            q.push([node.right, level + 1]) if node.right
        end
        result.push(level_vals)
    end

    result
end