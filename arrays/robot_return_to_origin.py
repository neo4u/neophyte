class Solution1:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count('R') == moves.count('L')) & \
                (moves.count('U') == moves.count('D'))

class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count('U') == moves.count('D'):
            if moves.count('L') == moves.count('R'):
                return True
        return False


import collections
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = collections.Counter(moves)
        return (counts['U'] == counts['D']) & (counts['L'] == counts['R'])


# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/description/
