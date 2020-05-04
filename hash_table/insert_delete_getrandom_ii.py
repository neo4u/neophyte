# Duplicate Allowed
import random
import collections


class RandomizedCollection:
    def __init__(self):
        self.nums, self.pos_map = [], collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.pos_map[val].add(len(self.nums) - 1)
        return len(self.pos_map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.pos_map[val]: return False

        i, last_val = self.pos_map[val].pop(), self.nums[-1]
        self.nums[i] = last_val

        self.pos_map[last_val].add(i)
        self.pos_map[last_val].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
