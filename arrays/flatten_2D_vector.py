from typing import List


class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.col = 0
        self.row = 0
        self.vec = v

    def next(self) -> int:
        if not self.hasNext(): return None

        result = self.vec[self.row][self.col]
        self.col += 1
        return result

    def hasNext(self) -> bool:
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True

            self.col = 0
            self.row += 1

        return False


# 251. Flatten 2D Vector
# https://leetcode.com/problems/flatten-2d-vector/description/

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
