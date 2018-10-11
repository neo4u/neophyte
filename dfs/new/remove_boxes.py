class Solution:
    def removeBoxes(self, boxes):
        def dfs(l, r, k):
            if l > r:
                return 0
            if (l, r, k) not in memo:
                while r > l and boxes[r] == boxes[r-1]:
                    k += 1
                    r -= 1
                while l < r and boxes[l] == boxes[r]:
                    k += 1
                    l += 1
                res = (k+1)**2 + dfs(l, r-1, 0)
                for i in range(l+1, r-1):
                    if boxes[i] == boxes[r]:
                        res = max(res, dfs(l, i, k+1) + dfs(i+1, r-1, 0))
                memo[l, r, k] = res
            return memo[l, r, k]
        memo = {}
        return dfs(0, len(boxes) - 1, 0)

# I found this solution in the score distribution.
# 89% 108ms
# memo[l, r, k] is the maximum points possible by removing the boxes[ l: r ] with k boxes outside boxes[ l : r ] that shares the same color as boxes[r].Because our recursion starts with dfs(0,len(boxes)-1, 0), so k doesn't include boxes[r] but the result does: res = (k+1)**2 + dfs(l, r-1, 0)

# The core recursion formula

#   if boxes[i] == boxes[r]:
#             res = max(res, dfs(l, i, k+1) + dfs(i+1, r-1, 0))
# We want all boxes[i] that has the same color as boxes[r] to be removed together, dfs(l, i, k+1) does just that.

# [1,3,1,3,3,1]
# In this example, i = 2, boxes[2] = boxes[5] = 1, dfs(1, 2, 2) => res = (k+1) ** 2 + dfs(1, 1,0) = 9 + 1 = 10

# Example: [1, 3, 1, 2, 1, 3, 1]
# memo:
# {(3, 3, 0): 1, (3, 4, 1): 5, (2, 5, 1): 9, (1, 1, 0): 1, (1, 2, 2): 10, (3, 4, 0): 2, (3, 5, 0): 3, (1, 2, 0): 2, (1, 3, 0): 3, (1, 2, 3): 17, (1, 4, 2): 18, (5, 5, 0): 1, (1, 6, 1): 19}
# Final ans: 19
# Let's focus on how we got (2, 5, 1): 9. 2th to 5th subarray is [1,2,1,3].
# boxes[r] = 3 and there is exactly one 3 in the rest of the array, that's why we have k = 1.

#     1. l=0, r=len(boxes)-1=6, because they are equal, l +=1, r -=1
#     2. l = 1, r = 5, boxes[l]= boxes[r] = 3
#     3. l = 2, r = 4, boxes[l] = boxes[r] = 1
#     4. l = r = 3, boxes[l] = 2
#     5. We return to the caller l = 2, r = 4, res = 2 ** 2 + 1 = 5, since l + 1= 3 = r - 1, we return to l = 1, r= 5, res = 2 ** 2 + 5 = 9
#         for i in range(2, 4):
#         if boxes[i] == boxes[5] = 3:
#         None of the box meets the condition, thus memo[2,5,1] = res = 9.
# Why is l = 2 instead of l = 1 as we have passed in, because we increment l when boxes[l] = boxes[r], remember that k is the number of boxes outside of boxes[ l : r] with the same color as boxes[r].