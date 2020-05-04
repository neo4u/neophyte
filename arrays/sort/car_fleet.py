from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - pos) / sp for pos, sp in cars]
        fleets = 0

        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:    fleets += 1
            else:                   times[-1] = lead

        return fleets + bool(times)


# 853. Car Fleet
# https://leetcode.com/problems/car-fleet/description/


# Approach 1: Sorting
# - Main idea is we use final position - curr position to get distance to be travelled by each car
# - We then use the distance / speed to get time required for each car to get to the destination
# - Now we have a list of times where car i takes times[i] units of time to get to the destination
# - We iterate through th

# 1. Sort 