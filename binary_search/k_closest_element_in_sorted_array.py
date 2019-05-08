# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/description/

class Solution:
    def findClosestElements(self, A, k, target):
        left, right = 0, len(A) - k

        while left < right:
            mid = (left + right) / 2
            if A[mid + k] - target < target - A[mid]:
                left = mid + 1
            else:
                right = mid

        return A[left:left + k]


# [1,2,3,4,5,9,10]
#  l
#  r

# k=4, target=3
# l = 0, r = 3
# mid = 1


# l 0, r = 1
# mid = 0
