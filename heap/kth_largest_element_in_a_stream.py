import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)

        return self.pool[0]
