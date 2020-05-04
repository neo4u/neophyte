class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.single_overlap = False


class MyCalendarTwo:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True

        if not self._can_insert(start, end, self.root): return False
        self._insert(start, end, self.root)
        return True

    def _can_insert(self, start, end, insert_root):
        if not insert_root: return True
        if start >= end: return True

        if end <= insert_root.start:   return self._can_insert(start, end, insert_root.left)    # Falls to the left
        elif start >= insert_root.end: return self._can_insert(start, end, insert_root.right)   # Falls to the right
        else:                                                                                   # Diff Types of Overlap
            if insert_root.single_overlap:                                  return False
            elif start >= insert_root.start and end <= insert_root.end:     return True
            else:
                a = min(insert_root.start, start)
                b = max(insert_root.start, start)
                c = min(insert_root.end, end)
                d = max(insert_root.end, end)
                return self._can_insert(a, b, insert_root.left) and self._can_insert(c, d, insert_root.right)

    def _insert(self, start, end, insert_root):
        if not insert_root:
            insert_root = Node(start, end)
            return insert_root
        if start >= end: return insert_root

        if start >= insert_root.end:   insert_root.right = self._insert(start, end, insert_root.right)
        elif end <= insert_root.start: insert_root.left = self._insert(start, end, insert_root.left)
        else:
            insert_root.single_overlap = True
            a = min(insert_root.start, start)
            b = max(insert_root.start, start)
            c = min(insert_root.end, end)
            d = max(insert_root.end, end)
            insert_root.start, insert_root.end = b, c
            insert_root.left, insert_root.right = self._insert(a, b, insert_root.left), self._insert(c, d, insert_root.right)

        return insert_root


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


# 731. My Calendar II
# https://leetcode.com/problems/my-calendar-ii/description/
