# Iterative
def swapPairs(self, head):
    dummy = ListNode(-1)
    dummy.next = head
    current = dummy

    while current.next != None and current.next.next != None:
        first = current.next
        second = current.next.next

        current.next = second
        first.next = second.next
        second.next = first

        current = current.next.next

    return dummy.next

# Recursive
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp

    return head