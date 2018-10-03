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
    q, result = [root], []
    
    while !q.empty?
        level, n = [], q.size
        n.times do |i|
            node = q.shift
            level << node.val
            q.push(node.left) if node.left
            q.push(node.right) if node.right
        end
        result.push(level)
    end

    result
end