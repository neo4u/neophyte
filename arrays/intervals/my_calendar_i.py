class Node:
    def __init__(self, s, e):
        self.start, self.end = s, e
        self.left, self.right = None, None


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self._insert(start, end, self.root)

    def _insert(self, s, e, insert_root):
        if e <= insert_root.start:
            if insert_root.left:
                return self._insert(s, e, insert_root.left)
            else:
                insert_root.left = Node(s, e)
                return True
        elif s >= insert_root.end:
            if insert_root.right:
                return self._insert(s, e, insert_root.right)
            else:
                insert_root.right = Node(s, e)
                return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i/description/


calendar = MyCalendar()
assert calendar.book(10, 20) == True
assert calendar.book(15, 25) == False
assert calendar.book(20, 30) == True
assert calendar.book(29, 31) == False
assert calendar.book(5, 9) == True
assert calendar.book(1, 6) == False
