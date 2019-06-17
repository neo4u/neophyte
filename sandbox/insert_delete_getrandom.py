import random

class RandomizedSet(object):
    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val in self.pos: return False

        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.pos: return False

        i, last = self.pos[val], self.nums[-1]
        self.nums[i], self.pos[last] = last, i

        self.nums.pop()
        self.pos.pop(val)

        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]




