# Do we want to optimize run time or memory?If we want to optimize run time then we can use a dictionary to pre-process the nums array. Simply create a map of key (number) and value (list of its indices). Then run reservoir sampling over this input.
# But the problem statement says that using too much memory is not allowed. In that case, we can iterate the entire array and keep a variable to track the frequency of the target for input into reservoir sampling.
# Notice random() returns uniform random number between [0 to 1]


from random import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt, index = 0, 0
        for idx, x in enumerate(self.nums):
            if x == target:
                cnt += 1
                if random() <= 1.0/(cnt):
                    index = idx
        return index



class Solution:

    def __init__(self, nums: List[int]):
        self.indexes = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.indexes[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indexes[target])

# https://leetcode.com/problems/random-pick-index/discuss/88071/C++_Time:-O(n)-Space:-O(n)_116ms_96.41_with-clear-explanation-by-probability

# 398. Random Pick Index
# https://leetcode.com/problems/random-pick-index/description/