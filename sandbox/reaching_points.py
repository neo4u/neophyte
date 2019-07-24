class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


class Solution2(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty == sy: return (tx - sx) % ty == 0
                tx %= ty
            else:
                if tx == sx: return (ty - sy) % tx == 0
                ty %= tx

        return tx == sx and ty == sy


class Solution3:
    def reachingPoints(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

        return sx == tx and sy <= ty and (ty - sy) % tx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % ty == 0

# 780. Reaching Points
# https://leetcode.com/problems/reaching-points/description/

# Steps:
# 1. Remove y from x as many times as possible (%=)
# 2. Similary x from y
# 3. Exit while as soon as x or y reaches dest or one of them overshoots
# 4. Based on which one reached or overshot check the corresponding counterpart for reachability

# Example
# 2, 3
# 11, 9
