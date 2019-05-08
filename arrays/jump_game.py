class Solution(object):
    def canJump(self, nums):
        i = 0
        stage = 0
        while i < len(nums) and i <= stage and stage < len(nums):
            stage = max(i + nums[i], stage)
            i += 1
        return i == len(nums) or stage >= len(nums) - 1


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