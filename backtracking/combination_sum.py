class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(0, candidates, target, [], result, 0)
        return result

    def helper(self, idx, candidates, target, so_far, result, sum_so_far):
        if sum_so_far == target:
            result.append([x for x in so_far])
        else:
            for i in range(idx, len(candidates)):
                if sum_so_far + candidates[i] <= target:
                    so_far.append(candidates[i])
                    self.helper(i, candidates, target, so_far, result, sum_so_far + candidates[i])
                    so_far.pop()
        return

# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c++-solution-use-backtracking-easy-understand.


# Approach 1: Gabbu, Backtracking
# 1. The most important clue in these questions is to build the recursion tree.
#    https://goo.gl/photos/u3RDJWAiPEWUYbH46
# 2. Also you need to remember to prune the tree,
#    else you run into maximum recursion depth issue.
# 3. We make use of the condition that all input numbers are positive.
#    This allows us to prune when adding the candidate[i] increases sum beyond target.
#    Since there are no negative numbers, we can safely stop at this point.
