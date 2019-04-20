


# 428. Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/

# Approach 1: DFS using pre-order for serialization and DFS and Queue for deserialization
# Steps:
# 1. Serialize using pre-order traversal using DFS and we use "#" as the end of children
#    for a parent
# 2. Deserialize by traversing the serialized tree string and using recursion. O(n).


# Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the function returns to its parent call.
# Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
# While the next item is not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
# Repeat until there are no more children, then ignore the "#".


# Approach 2: DFS using stack or iterative approach
# Time: O(n), visit n nodes once
# Space: O(n), store the entire tree in array and string
