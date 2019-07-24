class Solution(object):
    def canJump(self, nums):
        i = 0
        stage = 0
        while i < len(nums) and i <= stage and stage < len(nums):
            stage = max(i + nums[i], stage)
            i += 1
        return i == len(nums) or stage >= len(nums) - 1

class Solution:
    def canJump(self, nums):
        n = len(nums)
        last_good = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_good:
                last_good = i

        return last_good == 0

class Solution:
    def canJump(self, nums):
        n = len(nums)
        last_good = n - 1
        steps = 0

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last_good:
                if last_good != i:
                    steps += 1
                    last_good = i
                

        return last_good == 0


# Let's say the range of the current jump is [curBegin, curEnd],
# curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
# Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest,
# then keep the above steps, as the following:

# public int jump(int[] A) {
#   int jumps = 0, curEnd = 0, curFarthest = 0;

#   for (int i = 0; i < A.length - 1; i++) {
#       curFarthest = Math.max(curFarthest, i + A[i]);
#       if (i == curEnd) {
#           jumps++;
#           curEnd = curFarthest;
#       }
#   }
#   return jumps;
# }

              |         |



# 55. Jump Game
# https://leetcode.com/problems/jump-game/description/

# Input: [2,3,1,1,4]

# i = 0, stage = 0
# stage = max (2, 0) = 2

# i = 1, stage = 2
# stage = max(1 + 3, 2) = 4 

# i = 2, stage = 4
# stage = max(2 + 1, 4) = 4

# i = 3, stage = 4
# stage = max(3 + 1, 4) = 4

# i = 4, stage = 4
# stage = max(4 + 4, 4) = 8

# i == 5? true

# Input: [3,2,1,0,4]


# bool canJump(int A[], int n) {
#     int i = 0;
#     for (int reach = 0; i < n && i <= reach; ++i)
#         reach = max(i + A[i], reach);
#     return i == n;
# }