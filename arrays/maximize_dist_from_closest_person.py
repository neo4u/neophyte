class Solution:
    def maxDistToClosest(self, seats):
        n, dist = len(seats), -1
        res = [0] * n
       
        for i in range(n):
            if seats[i] == 1:
                dist = 0
            else:
                if dist == -1: continue
                dist += 1
                res[i] = dist

        dist = -1
        for i in range(n)[::-1]:
            if seats[i] == 1: dist = 0
            else:
                if dist == -1: continue
                dist += 1
                res[i] = dist if res[i] == 0 else min(res[i], dist)
        
        max_dist = 0
        for item in res:
            max_dist = max(max_dist, item)

        return max_dist


sol = Solution()
assert sol.maxDistToClosest([0,0,0,0,1])

[1,2,3,4,0]
[]