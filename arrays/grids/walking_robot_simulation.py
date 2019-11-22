from typing import List

# Intuitive and long
class Solution:
    def __init__(self):
        self.x, self.y = 0, 0
        self.curr_dir = 'n'
        self.dirs = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}
        self.code_to_dirs = {
            'nr': 'e', 'nl': 'w',
            'wr': 'n', 'wl': 's',
            'er': 's', 'el': 'n',
            'sr': 'w', 'sl': 'e'
        }
        self.obstacles = None
        self.result = 0

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd in {-2, -1}: self.change_dir(cmd)
            else: self.move(cmd)

        return self.result

    def move(self, cmd):
        for _ in range(cmd):
            dx, dy = self.dirs[self.curr_dir][0], self.dirs[self.curr_dir][1]

            if (self.x + dx, self.y + dy) in self.obstacles: break
            self.x += dx
            self.y += dy
        self.result = max(self.result, self.x**2 + self.y**2)

    def change_dir(self, cmd):
        turn = 'l' if cmd == -2 else 'r'
        code = self.curr_dir + turn

        self.curr_dir = self.code_to_dirs[code]


# Concise but non-descriptive
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, dx, dy = 0, 0, 0, 1
        obstacles = set(map(tuple, obstacles))
        result = 0

        for cmd in commands:
            if cmd == -1: dx, dy = dy, -dx
            elif cmd == -2: dx, dy = -dy, dx
            else:
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacles: break
                    x, y = x + dx, y + dy

            result = max(result, x * x + y * y)

        return result


# 874. Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/description/

# Intuition:
# - Here x, y represent cartesian co-ordinates and not indexes of 2-D array
# - So facing north would man dx, dy = 0, 1
