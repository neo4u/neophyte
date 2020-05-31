from typing import List


# Approach 1: Two Pass
class Solution2:
    def depth(self, nestedList):
        curr_depth = 1
        for x in nestedList:
            if not x.isInteger():
                curr_depth = max(curr_depth, 1+self.depth(x.getList()))
        return curr_depth

    def helper(self, nestedList, level, max_depth):
        for x in nestedList:
            if x.isInteger():
                self.d_sum = self.d_sum + x.getInteger()*(max_depth-level+1)
            else:
                self.helper(x.getList(), level+1, max_depth)
        return

    def depthSumInverse(self, nestedList: List['NestedInteger']) -> int:
        max_depth = self.depth(nestedList)
        self.d_sum = 0
        self.helper(nestedList, 1, max_depth)
        return self.d_sum


# Approach 2: 1 Pass with Cache
import collections
class Solution1:
    def depthSumInverse(self, nestedList: List['NestedInteger']) -> int:
        cache, self.max_level = collections.defaultdict(int), -1
        self.dfs(nestedList, 1, cache)
        total_sum = 0

        for lvl, total in cache.items():
            total_sum = total_sum + total * (self.max_level - lvl + 1)

        return total_sum

    def dfs(self, nestedList, level, cache):
        self.max_level = max(self.max_level, level)
        for x in nestedList:
            if x.isInteger():
                cache[level] += x.getInteger()
            else:
                self.helper(x.getList(), level+1, cache)
        return


# Approach 3: 1 Pass using a BFS like approach
class Solution:  # For leetcode OJ
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total_sum = 0
        level_sum = 0

        while nestedList:
            level_q = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    level_q.extend(x.getList())
            total_sum += level_sum
            nestedList = level_q

        return total_sum

class Solution: # For local Testing
    def depthSumInverse(self, nestedList: List['NestedInteger']) -> int:
        total_sum, level_sum = 0, 0

        while nestedList:
            next_level_list = []

            for x in nestedList:
                if type(x) is int:
                    level_sum += x
                    print(f'adding x: {x}, level_sum: {level_sum}')

                else:
                    for y in x:
                        next_level_list.append(y)

            total_sum += level_sum
            print(f'Adding level_sum to total: {total_sum}')
            nestedList = next_level_list

        return total_sum


# 364. Nested List Weight Sum II
# https://leetcode.com/problems/nested-list-weight-sum-ii/description/



# Approach 1: 2 Pass
# In the first pass, get the maximum depth of the nested list. The recursion is obvious - traverse the list and if there is any nestedList, find its depth. The final depth is the maximum depth from any nestedList.
# In the second pass, compute the sum using the same method as used in in the previous problem https://leetcode.com/problems/nested-list-weight-sum/

# Approach 2: 1 Pass with cache
# Engineer the solution like Nested List Weight Sum I, but store the sum at each level without any weights.
# Once completed, you will know the maximum level which will be the depth. Use that to do the computation for weighted sum.


# Approach 3: 1 Pass using BFS like approach

# Intuition:
# - level_sum is persistent across levels
# - thus each time level_sum gets added to the total_sum,
#   elements added in the previous levels get add once more
# - This ensures that they're adding proportional to their weightage that is deeper gets lower weightage,
#   by being added lesser number of times.

# Add all the integers at level to level_sum. Push all elements which are not interger (and are list type) into the list for next iteration. Make sure to flatten this list otherwise infinite loop.
# Now we only initilaize level_sum once. And successive level's integers are added to it. Once a level finishes, we add to total_sum. This naturally implements the multiplication logic - lower level sums are added multiple times to total sum.
# https://discuss.leetcode.com/topic/49041/no-depth-variable-no-multiplication/2


sol = Solution()
assert sol.depthSumInverse([[1,1], 2, [1,1]]) == 8
assert sol.depthSumInverse([1,[4,[6]]]) == 17
