# Segment tree implementation.
# Space complexity: O(2n)
# Time complexity: get O(2logn); check: O(1); release: O(logn).

class PhoneDirectory2(object):
    def __init__(self, max_number):
        self.tree = [True] * 2 * max_number
        self.max_number = max_number
    
    def get(self):
        if self.tree[1] == False: return -1
        i = 1
        while i < len(self.tree)/2:
            if 2 * i < len(self.tree) and self.tree[2 * i]:
                i = 2 * i
            if 2 * i + 1 < len(self.tree) and self.tree[2 * i + 1]:
                i = 2 * i + 1
                
        ret = i - self.max_number
       
        # update the tree
        self.tree[i] = False
        i /= 2
        while i > 0:
            self.tree[i] = self.tree[2 * i] or self.tree[2 * i + 1]
            i /= 2
        
        return ret
            
    def check(self, number):
        return number >= 0 and number < self.max_number and self.tree[number + self.max_number]
        
    def release(self, number):
        i = self.max_number + number
        while i > 0:
            self.tree[i] = True
            i /= 2

from bitarray import bitarray

class PhoneDirectory(object):
    def __init__(self, size):
        self.size = size
        self.ids = bitarray(size) # 0 is available, 1 is unavailable
        self.ids.setall(False)

    # O(n) can be optimized to log(n) by using segment tree
    def get(self):
        for idx, v in enumerate(self.ids):
            if not v:
                self.ids[idx] = True
                return idx
        else:
            raise Exception('overflow')

    # O(1)
    def release(self, num):
        if num > len(self.ids) or not self.ids[num]:
            raise Exception('invalid id')
        self.ids[num] = False

    # O(1)
    def check(self, num):
        return not self.ids[num]


d = PhoneDirectory(3);
assert d.get() == 0
assert d.get() == 1
assert d.check(2) == True
assert d.get() == 2
assert d.check(2) == False
d.release(2)
assert d.check(2) == True

d = PhoneDirectory(1_000_000)
assert d.get() == 0
assert d.get() == 1
assert d.get() == 2
assert d.check(2) == False
d.release(2)
assert d.check(2) == True
assert d.check(999_999) == True
