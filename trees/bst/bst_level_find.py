class Node:
    def __init__(self, value, level):
        self.left, self.right = None, None
        self.val, self.level = value, level

class BST:
    """
        Class to implement a binary search tree
        Usage:
        bst = BST()
        bst.insert(1); bst.insert(2); bst.insert(3); bst.insert(0)
    """
    def __init__(self):
        self.root = None

    def insert(self, value: int, insert_root: int = None):
        """
            Method to insert a value into a BST
                :param value:int: Represents the value to insert into BST
                :param insert_root:int=None: Represents the root of the sub-tree under which to insert node
        """
        # If there is no root, add the value at root, and set the self.root
        if not self.root:
            self.root = Node(value, 1)
            return self.root.level

        # If insert_root is not set, set it to root, this is the default behavior
        if not insert_root: insert_root = self.root

        # if value already exiists in the BST, we can't have duplicates
        if value == insert_root.val: return insert_root.level
        # If value is less than the curr node's value then it should go to its left
        elif value < insert_root.val:
            # if left sub-tree exists, we just pass the value to be inserted into left-subtree recursively
            # and so we pass the root of the left sub-tree which is insert_root.left
            if insert_root.left: return self.insert(value, insert_root.left)
            insert_root.left = Node(value, insert_root.level + 1)
            return insert_root.left.level
        # If value is greater than the curr node's value then it should go to its right
        elif value > insert_root.val:
            # if right sub-tree exists, we just pass the value to be inserted into right-subtree recursively
            # and so we pass the root of the right sub-tree which is insert_root.right
            if insert_root.right: return self.insert(value, insert_root.right)
            insert_root.right = Node(value, insert_root.level + 1)
            return insert_root.right.level


def solve(A, N):
    # Return a list of N elements, ith element representing level of A[i]
    # Write your code here
    bst = BST()
    return [bst.insert(val) for val in A]


# # N = int(input())
# # A = list(map(int, input().split()))
# N = 7
# A = [15, 9, 7, 8, 2, 19, 10]

# out_ = solve(A, N)
# print(' '.join(map(str, out_)))


assert solve([15, 9, 7, 8, 2, 19, 10], 7) == [1, 2, 3, 4, 4, 2, 3]
