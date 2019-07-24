from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# Approach 1: DFS Recursive using pre-order traversal
class Codec:
    # Serialization
    def dfs_serialize(self, node, pre_order):
        if not node: return
        pre_order.append(str(node.val))
        for child in node.children:
            self.dfs_serialize(child, pre_order)
        pre_order.append("#")                       # indicates no more children, continue serialization from parent

#      1
#   2 3 4 
# 456

# [1, 2, 4, '#', 5, '#', 6, '#', '#', 3, '#', 4, '#', '#']


    def serialize(self, root):
        pre_order = []
        self.dfs_serialize(root, pre_order)
        return ",".join(pre_order)

    def deserialize(self, data):
        if not data: return None

        pre_order = deque(data.split(","))
        root = Node(int(pre_order.popleft()), [])
        self.dfs_deserialize(root, pre_order)
        return root

# []

    # Deserialization
    def dfs_deserialize(self, node, pre_order):
        if not pre_order: return
        while pre_order[0] != "#":                  # add child nodes with subtrees
            value = pre_order.popleft()
            child = Node(int(value), [])
            node.children.append(child)
            self.dfs_deserialize(child, pre_order)

        pre_order.popleft()                         # discard the "#"


# Approach 2: BFS Iterative using pre-order traversal and a queue, Faster on Leetcode inputs
class Codec:
    def serialize(self, root):
        if root == None: return ''
        pre_order = [str(root.val)]
        queue = deque([root])
        while queue:
            front = queue.popleft()
            if len(front.children) > 0:
                queue.extend(front.children)
                serialized_children = [str(child.val) for child in front.children]
                pre_order.append(','.join(serialized_children))
            else:
                pre_order.append('')

        return ';'.join(pre_order)

    def deserialize(self, data):
        if len(data) == 0: return None
        pre_order = deque(data.split(';'))
        root = Node(int(pre_order.popleft()), [])
        queue = deque([root])

        while queue:
            node = queue.popleft()
            serialized_children = pre_order.popleft()
            if len(serialized_children) > 0:
                values = [int(child) for child in serialized_children.split(',')]
                children = []
                for val in values: children.append(Node(val, []))
                node.children = children
                queue.extend(children)

        return root


# 428. Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/

# Approach 1: DFS using pre-order for serialization and DFS and Queue for deserialization
# Steps:
# 1. Serialize using pre-order traversal using DFS and we use "#" as the end of processing of children for a parent
# 2. Deserialize by traversing the serialized tree string, recursively and popping from front of the queue. O(n).

# Approach 2: DFS using stack or iterative approach
# Time: O(n), visit n nodes once
# Space: O(n), store the entire tree in array and string

# Example 1
#      1
#    /   \
#   2     3
#       / | \
#      4  5  6
r1, r2, r3 = Node(4, []), Node(5, []), Node(6, [])
l, r = Node(2, []), Node(3, [r1, r2, r3])
root = Node(1, [l, r])

codec = Codec()
assert codec.serialize(root) == "1,2,#,3,4,#,5,#,6,#,#,#"
new_root = codec.deserialize("1,2,#,3,4,#,5,#,6,#,#,#")

assert new_root.val == root.val
seta = map(lambda child: child.val, new_root.children)
setb = map(lambda child: child.val, root.children)
assert list(seta) == list(setb)
set_b1 = map(lambda child: child.val, new_root.children[1].children)
set_b2 = map(lambda child: child.val, r.children)
assert list(set_b1) == list(set_b2)

# Example 2
#     1
#  /  |  \
# 2   3   4
#   /   \
#  5     6
c5, c6 =  Node(5, []), Node(6, [])
c2, c3, c4 = Node(2, []), Node(3, [c5, c6]), Node(4, [])
root = Node(1, [c2, c3, c4])

codec = Codec()
assert codec.serialize(root) == "1,2,#,3,5,#,6,#,#,4,#,#"
new_root = codec.deserialize("1,2,#,3,5,#,6,#,#,4,#,#")

assert new_root.val == root.val
set_a = map(lambda child: child.val, new_root.children)
set_b = map(lambda child: child.val, root.children)
assert list(seta) == list(setb)
set_b1 = map(lambda child: child.val, new_root.children[1].children)
set_b2 = map(lambda child: child.val, c3.children)
assert list(set_b1) == list(set_b2)