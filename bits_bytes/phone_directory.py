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
        self.ids.setall(0)

    # O(log(n))
    def get(self):
        l, r = 0, self.size

        while l < r:
            mid = l + (r - l) // 2
            if not self.ids[mid]:
                r = mid
            else:
                l = mid + 1

        self.ids[l] = 1
        return -1 if l == self.size else l + 1

    # O(1)
    def release(self, num):
        if num > len(self.ids) or not self.ids[num - 1]:
            raise Exception('invalid id')
        self.ids[num - 1] = False

    # O(1)
    def check(self, num):
        return not self.ids[num - 1]


d = PhoneDirectory(3);
assert d.get() == 1
assert d.check(1) == False

assert d.get() == 2
assert d.check(2) == False
d.release(2)
assert d.check(2) == True

assert d.get() == 2
assert d.check(2) == False

assert d.check(3) == True
assert d.get() == 3
assert d.check(3) == False



d = PhoneDirectory(1_000_000_000)
assert d.get() == 1
assert d.check(1) == False

assert d.get() == 2
assert d.check(2) == False

assert d.get() == 3
assert d.check(3) == False

d.release(2)
assert d.check(2) == True

assert d.get() == 2
assert d.get() == 4

d.release(1)
d.release(2)
d.release(3)
d.release(4)

for i in range(1_000_000_000):
    assert d.get() == i + 1

assert d.check(1_000_000_000) == False
