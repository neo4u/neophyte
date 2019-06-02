class Node:
    def __init__(self, s, e):
        self.s, self.e = s, e
        self.left, self.right = None, None
        self.booked = False

class MyCalendarTwo:
    def __init__(self):
        self.root = None

    def book(self, s, e):
        if not self._insertable(s, e, self.root): return False

        self.root = self._insert(s, e, self.root)
        return True

    def _insertable(self, s, e, insert_root):
        if not insert_root: return True
        if s >= e: return True

        if e <= insert_root.s:
            return self._insertable(s, e, insert_root.left)
        elif s >= insert_root.e:
            return self._insertable(s, e, insert_root.right)
        else:
            if insert_root.booked:
                return False
            elif s >= insert_root.s and e <= insert_root.e:
                return True
            else:
                return self._insertable(s, insert_root.s, insert_root.left) and self._insertable(insert_root.e, e, insert_root.right)

    def _insert(self, s, e, insert_root):
        if not insert_root:
            insert_root = Node(s, e)
            return insert_root
        if s >= e: return insert_root

        if e <= insert_root.s:
            insert_root.left = self._insert(s, e, insert_root.left)
        elif s >= insert_root.e:
            insert_root.right = self._insert(s, e, insert_root.right)
        else:
            insert_root.booked = True
            a = min(insert_root.s, s)
            b = max(insert_root.s, s)
            c = min(insert_root.e, e)
            d = max(insert_root.e, e)

            insert_root.s, insert_root.e = b, c
            insert_root.left, insert_root.right = self._insert(a, b, insert_root.left), self._insert(c, d, insert_root.right)

        return insert_root
