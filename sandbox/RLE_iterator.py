from typing import List

class RLEIterator:
    def __init__(self, A: List[int]):
        self.rle = A
        self.freq = A[0]
        self.num = A[1]
        self.idx = 2

    def next(self, n: int) -> int:
        while self.freq < n and self.has_next():
            n -= self.freq
            self.freq = 0

        if self.freq >= n:
            self.freq -= n
            return self.num

        return -1

    def has_next(self):
        while self.idx <= len(self.rle) - 2 and self.freq == 0:
            self.freq = self.rle[self.idx]
            self.num = self.rle[self.idx + 1]
            self.idx += 2

        return self.freq != 0


class RLEIterator2:
    def __init__(self, A: List[int]):
        self.pointer = 0
        self.A = A

    def next(self, n: int) -> int:
        while self.pointer < len(self.A):
            self.A[self.pointer] -= n
            if self.A[self.pointer] >= 0:
                return self.A[self.pointer+1]
            n = -self.A[self.pointer]
            self.pointer += 2
        return -1
                