class Solution:
    def findRadius(self, houses, heaters):
        prev, heaters, radius, count = None, set(heaters), 0, 0
        for h in houses:
            if h in heaters:
                i = h - 1
                if prev is None:
                    radius = i
                else:
                    radius = max(radius, (i - prev) // 2)
                count += 1
                prev = i
        if count == 1:
            radius = max(radius, prev)  # left radius
            radius = max(radius, len(houses) - 1 - prev)
        return radius
