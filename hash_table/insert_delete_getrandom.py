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


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
