class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# [1,3,4,2,2]


# 1 -> 3 -> 2 -> 4
#           ^    |
#           |____|

# 1->2->3->4->5->6->3

# [1,2,4,3,2]

# 1-> 2 -> 4
#      ^    |
#      |____|


# [1,4,2,3,2]

# 1->4->2->2

# [3,1,2,0]

# 3 -> 