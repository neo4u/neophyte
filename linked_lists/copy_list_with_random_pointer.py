
# Approach 1: DFS with Hash Space: O(n)
# Example
# 1 -> 2 -> 3
# r    r    r
# 2	 2    1
  
# // clone(1, [])
# 	// add [1]
# 	// clone(2, [1])
# 		//	add [1, 2]
#         //  clone(3, [1,2])
# 			// add [1,2,3]
#             // clone(nil, [1,2,3])
# 			// clone(1, [1,2,3])
# 			// return cloned as 1 is in map
  		       
#   		// clone n -> nil
#         	  // r-> clone_1
# 	// 2 n->clone_3
#   	// 2 r->clone(2, [1,2,3])
#   	  // return cloned
# 	// r -> clone(2, [1,2,3])
#     // return cloned



# Approach 3: Iterative O(1)
class Solution(object):
    def copyRandomList(self, head):
        if not head: return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:
            new_node = Node(ptr.val, None, None)

            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        new_head = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return new_head