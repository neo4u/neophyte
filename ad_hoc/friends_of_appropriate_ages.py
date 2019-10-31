class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages: count[age] += 1

        result = 0
        for ageA, countA in enumerate(count):
            if ageA == 0: continue
            for ageB, countB in enumerate(count):
                if ageB == 0: continue

                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue

                if ageA == ageB:    result += countA * (countA - 1)
                else:               result += countA * countB

        return result


# 825. Friends Of Appropriate Ages
# https://leetcode.com/problems/friends-of-appropriate-ages/description/


# Intuition
# - Instead of processing people which can get larget.
# - We can process pairs of (age, count) representing how many people are that age.
# - Since there are only 120 possible ages, this is a much faster loop.

# Steps:
# 1. For each pair (ageA, countA), (ageB, countB), if the conditions are met,
#    then countA * countB pairs of people made friend requests
#    as all ageA, ageB send requests to each other
# 2. If ageA == ageB, then we overcounted: we should have countA * (countA - 1)
#    pairs of people making friend requests instead, as you cannot friend request yourself.
