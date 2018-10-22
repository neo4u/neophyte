# two pointers:
class Solution(object):
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res


# use dictionary to count:
class Solution1(object):
    def intersect(self, nums1, nums2):
        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res


# use Counter to make it cleaner:
class Solution2(object):
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res


# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Approaches
# Where n is the combined length of both arrays
# Approach 1: Using two sets Time: O(n) Space: O(n)
# Approach 2: Using a hash, Time: O(n) Space: O(n)
# Approach 3: Binary search, iterate through one and sort and do binary search on the other, Time: O(nlog(n)), Space: O(1)
# Approach 4: Two pointer (java) or using first/last and shift (ruby), Time: O(nlog(n)), Space: O(1)

# Follow-up questions
# 1. What if the given array is already sorted? How would you optimize your algorithm?
# 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 3. What if elements of nums2 are stored on disk, and the memory is
# limited such that you cannot load all elements into the memory at once?

# Answer for 3. If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
# read chunks of array that fit into the memory, and record the intersections.
# If both nums1 and nums2 are so huge that neither fit into the memory,
# sort them individually (external sort https://en.wikipedia.org/wiki/External_sorting),
# then read 2 elements from each array at a time in memory, record intersections.

# I think the goal of this question is to test whether the
# interviewee understands some of the data engineering techniques.
# From a data engineer's perspective, basically there are three ideas to solve the question:
# 1. Store the two strings in distributed system (whether self designed or not),
#    then using MapReduce technique to solve the problem;
# 2. Processing the Strings by chunk, which fits the memory,
#    then deal with each chunk of data at a time;
# 3. Processing the Strings by streaming, then check.