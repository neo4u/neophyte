class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


class Monarchy:
    def __init__(self, king_name):
        self.root = king_name
        self.names_map = {king_name: Node(king_name)}

    def birth(self, name, parent):
        node = self.names_map[parent]
        child = Node(name)
        node.children.append(child)
        self.names_map[name] = node

    def death(self, name):
        node = self.names_map[name]
        if node == self.root:
            first_c = self.root.children.pop(0)
            self.root = first_c
            first_c.children.extend(self.root.children)

        for n in self.root.children:
            if self._delete(node, n, self.root):
                break

    def _delete(self, delete_node, node, parent):
        if node == delete_node:
            i = parent.children.index(node)
            for c in node.children:
                parent.children.insert(i, c)
                i += 1
            return True

        for c in node.children:
            if self._delete(delete_node, c, node):
                return True

        return False

    def get_order_of_succession(self):
        self._dfs(self.root)

    def _dfs(self, node):
        print(node.name)
        for c in node.children:
            self._dfs(c)


#    1
# 4      5        3
#               6    7
