import random
class RandomizedSet:
    def __init__(self):
        self.nums, self.pos_map = [], {}

    def insert(self, val: int) -> bool:
        if val in self.pos_map: return False

        self.nums.append(val)
        self.pos_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos_map: return False

        i, last_val = self.pos_map[val], self.nums[-1]
        self.nums[i], self.pos_map[last_val] = last_val, i

        self.nums.pop()
        self.pos_map.pop(val)

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/


# Intuition
# Using Array
# - To get O(1) on insert() is easy, we can just append it at the end
# - To get O(1) on get_random() is easy cuz we get generate a random number between 1...n and access that index on array
# - To get O(1) on remove() is hard cuz we have to remove in the middle of contiguous memory block

# Using Dictionary
# - To get O(1) on insert() and remove() is easy and is the nature of a dictionary
# - To get O(1) on get_random() is hard cuz we can't access random index element from a dict
