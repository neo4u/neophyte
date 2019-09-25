class Node:
    def __init__(self, value, level):
        self.left, self.right = None, None
        self.val, self.level = value, level

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value, insert_root=None):
        if not self.root:
            self.root = Node(value, 1)
            return self.root, self.root.level

        if not insert_root: insert_root = self.root

        if value == insert_root.val: return insert_root, insert_root.level
        elif value < insert_root.val:
            if not insert_root.left:
                insert_root.left = Node(value, insert_root.level + 1)
                return insert_root.left, insert_root.left.level
            else:
                return self.insert(value, insert_root.left)
        elif value > insert_root.val:
            if not insert_root.right:
                insert_root.right = Node(value, insert_root.level + 1)
                return insert_root.right, insert_root.right.level
            else:
                return self.insert(value, insert_root.right)


def solve(A, N):
    # Return a list of N elements, ith element representing level of A[i]
    # Write your code here
    bst = BST()
    return [bst.insert(val)[1] for val in A]


# # N = int(input())
# # A = list(map(int, input().split()))
# N = 7
# A = [15, 9, 7, 8, 2, 19, 10]

# out_ = solve(A, N)
# print(' '.join(map(str, out_)))


assert solve([15, 9, 7, 8, 2, 19, 10], 7) == [1, 2, 3, 4, 4, 2, 3]
