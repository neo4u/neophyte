# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

# tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
# For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

# len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
# len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
# len = 3   :      [4, 5, 6]            => tails[2] = 6
# We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

# Each time we only do one of the two:

# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
# Doing so will maintain the tails invariant. The the final answer is just the size.


# MOre detailed explanation:
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step

def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

# Runtime: 48 ms


# My base idea comes from:https://leetcode.com/problems/increasing-triplet-subsequence/description/
# in that problem, the idea is:

# 1.initial sub = [max, max], we use a list of length 2 to store the subsequence, or smaller value which may form the new subsequence.
# 2. traversing the nums：
#     a) if val <= sub[0], then we update sub[0] = val.
#     b) else if sub[0] < val <= sub[1], the we update sub[1] = val.
#     c) else: sub[1] < val, we find a 3 length subsequence. done!
# The key to understanding this solution is if we have found a subsequence of length 2. If the next element is larger than sub[1], then a subsequence of length 3 is found. If the next element is smaller than sub[0] or sub[1], then we find a part of a new subsequence and save it. At the same time, the known subsequence length is 2.

# Here is the solution's track, say we have nums = [9, 7, 10, 1, 8, 9].

# i = 0:    sub = [9, max];
# i = 1:    sub = [7, max];
# i = 2:    sub = [7, 10];
# i = 3:    sub = [1, 10];
# i = 4:    sub = [1, 8];
# i = 5:    sub[1] < 9, done.
def increasingTriplet(self, nums):
        sub = [float('inf'), float('inf')]
        for n in nums:
            if n <= sub[0]:
                sub[0] = n
            elif n <= sub[1]:
                sub[1] = n
            else:
                return True
        return False
# So back to this question, the idea extends to:

# 1. initial sub = [ ].
# 2. traversing the nums:
#     a) if val > sub's all elements, then subsequence length increased by 1, sub.append(val);
#     b) if sub[i-1] < val < sub[i], then we find a smaller value, update sub[i] = val. Some of the elements stored in the sub[ ] are known subsequences, and the other part is elements of other possible new subsequences. However, the length of the known subsequences is unchanged.
   
# 3. return the sub[ ]'s length.
# Here is the solution's track, as we have nums = [8, 2, 5, 1, 6, 7, 9, 3],when we traversing the nums:

# i = 0,    sub = [8]
# i = 1,    sub = [2]
# i = 2,    sub = [2, 5]
# i = 3,    sub = [1, 5],    # element has been changed, but the sub's length has not changed.
# i = 4,    sub = [1, 5, 6]
# i = 5,    sub = [1, 5, 6, 7]
# i = 6,    sub = [1, 5, 6, 7, 9]
# i = 7,    sub = [1, 3, 6, 7, 9]    #done! Although the elements are not correct, but the length is correct.

# # O(n*m) solution. m is the sub[]'s length
def lengthOfLIS(self, nums):
        sub = []
        for val in nums:
            pos , sub_len = 0, len(sub)
            while(pos <= sub_len):    # update the element to the correct position of the sub.
                if pos == sub_len:
                    sub.append(val)
                    break
                elif val <= sub[pos]:
                    sub[pos] = val
                    break
                else:
                    pos += 1
        
#         return len(sub)
# Because of sub[ ] is incremental, we can use a binary search to find the correct insertion position.

# # O(nlogn) solution with binary search
def lengthOfLIS(self, nums):

        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)