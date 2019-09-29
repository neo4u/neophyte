# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} pre
# @param {Integer[]} post
# @return {TreeNode}
def construct_from_pre_post(pre, post)
    return nil if pre.nil? || post.nil? || pre.empty? || post.empty?
    root = TreeNode.new(pre[0])

    return root if post.size == 1
    idx = pre.find_index(post[-2])
    root.left = construct_from_pre_post(pre[1...idx], post[0...idx - 1])
    root.right = construct_from_pre_post(pre[idx...pre.size], post[idx - 1...pre.size - 1])

    root
end

#      1
#   2     3
# 4  5

# pre: 1   2 4 5    3
# pos: 4 5 2     3       1
