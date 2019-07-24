import random

class RandomizedSet(object):
    def __init__(self):
        self.nums, self.pos_map = [], {}

    def insert(self, val):
        if val in self.pos_map: return False

        self.nums.append(val)
        self.pos_map[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.pos_map: return False

        i, last = self.pos_map[val], self.nums[-1]
        self.nums[i], self.pos_map[last] = last, i

        self.nums.pop()
        self.pos_map.pop(val)

        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]


# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
