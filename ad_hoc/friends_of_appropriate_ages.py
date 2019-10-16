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

                if ageA == ageB:
                    result += countA * (countA - 1)
                else:
                    result += countA * countB

        return result


# 825. Friends Of Appropriate Ages
# https://leetcode.com/problems/friends-of-appropriate-ages/description/
