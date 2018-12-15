class Solution(object):
    def helper(self, i, k, so_far, target, all_results):
        if sum(so_far) == target and len(so_far) == k:
            all_results.append([x for x in so_far])
        elif i == 10 or k == len(so_far):
            return
        else:
            for x in range(i,10):
                if sum(so_far) + x <= target:
                    so_far.append(x)
                    self.helper(x+1, k, so_far, target, all_results)
                    so_far.pop()
            return
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        all_results = []
        self.helper(1, k, [], n, all_results)
        return all_results

# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

# Approach 1: Backtracking
# Similar to problem Combination Sum 1 and 2.
# Draw the recursion tree.
# Then identify the boundary/terminating conditions i.e. pruning the tree.

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        l = list(range(1,10))
        rl = []
        self.backTracking(l, k, n, 0, [], 0, rl)
        return rl
    
    def backTracking(self, l, k, n, index, tl, sums, rl):
        if len(tl) == k and sums == n:
            rl.append(tl)
            return True

        while index < len(l):
            newSums = sums + l[index]
            if newSums <= n and len(tl) < k:
                sl = tl + [l[index]]
                self.backTracking(l, k, n, index + 1, sl, newSums, rl)
            index += 1

# Here's how I optimized:
# 1.Do not call backTracking when the current tl's length is greater than k
# 2.Do not make any copy of the original 1 to 9 list,which means avoid slice operation
# 3.I use additional parameter newSums to store the sum result