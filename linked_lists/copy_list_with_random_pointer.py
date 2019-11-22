class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# Approach 3: Iterative O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head

        # Creating a new weaved list of original and copied nodes.
        # create and interweave
        ptr = head
        while ptr:
            clone = Node(ptr.val, None, None)
            clone.next = ptr.next
            ptr.next = clone
            ptr = clone.next

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.

        # Copy random ptr data
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'

        # Unweave
        ptr_old = head          # A->B->C
        ptr_new = head.next     # A'->B'->C'
        new_head = head.next
        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return new_head



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return

        self.cloned = {}
        self.dfs(head)
        return self.cloned[head]

    def dfs(self, node):
        if not node: return
        if node in self.cloned: return self.cloned[node]

        clone = Node(node.val, None, None)
        self.cloned[node] = clone

        clone.next = self.dfs(node.next)
        clone.random = self.dfs(node.random)

        return clone

# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Approach 1: Hash Map for storing cloned mapping
# Similar to clone graph

# Approach 2: without hash map and using interweaved copy nodes

# Key Insight:
# 1. No hash map needed
# 2. Just store clones after the originals like this for A->B->C: A->A'->B->B'->C->C'

# Steps:
# 1. Interweave
# 2. Copy random ptr
# 3. Unweave


# Time: O(n)
# Space: O(1)
