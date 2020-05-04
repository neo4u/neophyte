class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.ht = [None for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % self.capacity

        if not self.ht[i]:
            self.ht[i] = Node(key, value)
        else:
            curr = self.ht[i]
            prev = None

            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev = curr
                curr = curr.next

            prev.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.capacity

        if not self.ht[i]:
            return -1
        else:
            curr = self.ht[i]

            while curr:
                if curr.key == key: return curr.val
                curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.capacity
        if not self.ht[i]: return

        curr = self.ht[i]
        dummy = prev = Node(None, None)
        prev.next = curr

        while curr:
            if curr.key == key:
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next

        self.ht[i] = dummy.next


# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/description/
