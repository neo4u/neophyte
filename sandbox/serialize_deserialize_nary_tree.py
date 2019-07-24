class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root) -> str:
        pre_order = []
        self.dfs_serialize(root, pre_order)
        return ",".join(pre_order)

    def dfs_serialize(self, node, pre_order):
        if not node: return None
        pre_order.append(str(node.val))

        for child in node.children:
            self.dfs_serialize(child, pre_order)

        pre_order.append("#")

    def deserialize(self, data):
        if not data: return None

        pre_order = data.split(",")
        root = Node(int(pre_order.pop(0)), [])
        self.dfs_deserialize(root, pre_order)

    def dfs_deserialize(self, node, pre_order):
        if not pre_order: return None

        while pre_order[0] != "#":
            val = int(pre_order.pop(0))
            child = Node(val, [])
            node.children.append(child)
            self.dfs_deserialize(child, pre_order)

        pre_order.pop(0)


#          1
#     2    3    4
#   5


# pre_order: [1, 2, 5, #, #, 3, #, 4, #, #]
# dfs(1, [2, 5, #, #, 3, #, 4, #, #])
    # node 1
    #     child 2
    #     dfs(2, [5, #, #, 3, #, 4, #, #])
    #         child 5
    #         dfs(5, [#, 3, #, 4, #, #])
