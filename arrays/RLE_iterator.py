class RLEIterator(object):
    def __init__(self, A):
        self.A = A
        self.i = 0
        self.q = 0

    def next(self, n):
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i+1]

        return -1
