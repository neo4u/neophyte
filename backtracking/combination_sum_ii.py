# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/

# Iterative
def combinationSum2(self, candidates, target):
    # Sorting is really helpful, se we can avoid over counting easily
    candidates.sort()                      
    result = []
    self.combine_sum_2(candidates, 0, [], result, target)
    return result

def combine_sum_2(self, nums, start, path, result, target):
    # Base case: if the sum of the path satisfies the target, we will consider 
    # it as a solution, and stop there
    if not target:
        result.append(path)
        return
    
    for i in xrange(start, len(nums)):
        # Very important here! We don't use `i > 0` because we always want 
        # to count the first element in this recursive step even if it is the same 
        # as one before. To avoid overcounting, we just ignore the duplicates
        # after the first element.
        if i > start and nums[i] == nums[i - 1]:
            continue

        # If the current element is bigger than the assigned target, there is 
        # no need to keep searching, since all the numbers are positive
        if nums[i] > target:
            break

        # We change the start to `i + 1` because one element only could
        # be used once
        self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                           result, target - nums[i])


# Approach 1: Gabbu, Backtracking

# 1. Recursion tree will help you solve this problem. https://goo.gl/photos/vEDezZoWctf7CgfM8
# 2. Combination Sum I allowed duplicates. To avoid those, in the recursive call, use i + 1.
# 3. Now other duplicates are also possible. Imagine [1,2,5, 7, 1] and target as 8.
#    If we use DFS we will get [1,7] and then [7,1]. How do we avoid this?
# 4. Sort candidates: [1,1,2,5,7]. Now when you start with index 0,
#    your first element will be 1. It will allow you to pick the second element as 1 too.
#    You will be able to pick [1,7]. But during recursion, when you reach the next start index as 1,
#    your recursion tree will again start from 1. This will lead to a duplicate [1,7].
#    You want to avoid this.

# Another Implementation
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        all_solns = []
        self.helper([], 0, sorted(candidates), target, all_solns)
        return all_solns

    def helper(self, so_far, k, nums, target, all_solns):
        sum_so_far = sum(so_far)
        if sum_so_far == target:
            all_solns.append([x for x in so_far])
        else:
            for i in range(k, len(nums)):
                if i > k and nums[i] == nums[i-1]:
                    continue
                if (sum_so_far + nums[i] <= target):
                    so_far.append(nums[i])
                    self.helper(so_far, i+1, nums, target, all_solns)
                    so_far.pop()
        return
