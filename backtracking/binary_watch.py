from typing import List
from itertools import combinations





# Approah 
class Solution1:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []

        for hrs in range(0, min(num, 4) + 1):               # Choose 0...min(num, 4) as the number of hour LEDs
            mins = num - hrs                                # Rest will be mins LEDs
            if not 0 <= mins <= 6: continue                 # Prune combinations where mins LEds are not between [0, 6]

            hr_led_combos = combinations(range(4), hrs)     # Generate all possible combinations of hour LEDs
            mn_led_combos = combinations(range(6), mins)    # Generate all possible combinations of mins LEDs

            hr_values = tuple(map(lambda hs: sum(2 ** i for i in hs), hr_led_combos))
            mn_values = tuple(map(lambda ms: sum(2 ** i for i in ms), mn_led_combos))

            for h in hr_values:
                for m in mn_values:
                    if h >= 12 or m >= 60: continue
                    result.append('%d:%02d' % (h, m))
            # the 4 lines above can be written as below:
            # result += ['%d:%02d' % (h, m) for h in hr_values for m in mn_values if h < 12 and m < 60]


        return result

# Approach 2: Backtracking
class Solution2:
    def readBinaryWatch(self, num):
        nums = [1, 2, 4, 8, 16, 32, 100, 200, 400, 800]
        result = []
        self.dfs(nums, 0, 0, num, 0, result)
        return result

    def dfs(self, nums, level, idx, num, path, result):
        if level == num:
            hrs, mins = path // 100, path % 100

            if hrs > 11 or mins > 59: return
            elif mins < 10:           return result.append(str(hrs) + ":" + "0" + str(mins))
            else:                     return result.append(str(hrs) + ":" + str(mins))

        for i in range(idx, len(nums)):
            self.dfs(nums, level + 1, i + 1, num, path + nums[i], result)


# Approach 3: With combinations and BT
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        self.result = []
        self.bt(num, 0)
        return self.result

    def bt(self, num, hours):
        if hours > num: return

        for hr_combo in combinations([1, 2, 4, 8], hours):
            hs = sum(hr_combo)
            if hs >= 12: continue
            for mins_combo in combinations([1, 2, 4, 8, 16, 32], num - hours):
                mins = sum(mins_combo)
                if mins >= 60: continue
                self.result.append("%d:%02d" % (hs, mins))

        self.bt(num, hours + 1)


# 401. Binary Watch
# https://leetcode.com/problems/binary-watch/description/

# Intuition
# 1. Number of hour LEDs switched on can vary between 0 ... 4
# 2. Number of mins LEDs switched on can vary between 0 ... 6
# 3. Given n LEDs that are switched on, We have to split the lights between hours and mins,
#    So if we're given a total n switched on lights out of 10,
#    and if we have x hour LEDs as switched on,
#    then n - x LEDs are left to be used to represent mins
# 4. We have to generate all possible combinations of hours represented by x LEDs
# 5. We have to generate all possible combinations of mins represented by n - x LEDs
# 6. Then generate all combinations from each hour value and each min value

# Time: O(1), Due to fixed number of combinations
# Space: O(1), Due to fixed number of combinations


# Approach 1: With combinations
# Steps:
# 1. Choose 0...min(num, 4) as the number of hour LEDs, Rest will be mins LEDs
# 2. Generate all possible combinations of hour LEDs
# 3. Generate all possible combinations of mins LEDs
# 4. Use the hour LEDs combos to derive the hour values represented by those LED combos
# 5. Use the mins LEDs combos to derive the mins values represented by those LED combos
# 6. Combine all possible hour values with all possible mins values
# 7. Prune bad combinations, to only keep valid hour and mins values


# Approach 2: Backtracking
# Use Helper arrays to help us to represent binary numbers.
# hours * 100 to distinguish that from minutes.
# then just easy and normal dfs to retrieve all combinations. 

# Approach 3: Using combinations and Backtracking



sol = Solution()
assert sol.readBinaryWatch(1).sort() == [
    "1:00", "2:00", "4:00",
    "8:00", "0:01", "0:02",
    "0:04", "0:08", "0:16", "0:32"
].sort()