from typing import List
import collections


# Approach 1: Using a hash, Time: O(n) Space: O(n)
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res

# Approach 1: Using a hash, But using Counter, Time: O(n) Space: O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        if m < n: nums1, nums2, m, n = nums2, nums1, n, m   # Ensure that the bigger one is nums1 so that memory is high and time is now
        h1, result = collections.Counter(nums1), []
        for num in nums2:
            if num not in h1: continue
            result.append(num)
            h1[num] -= 1
            if h1[num] == 0: h1.pop(num)
        return result


# Approach 3: Two pointer, Time: O(nlog(n)), Space: O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n, i, j, result = len(nums1), len(nums2), 0, 0, []
        nums1, nums2 = sorted(nums1), sorted(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:     i += 1
            elif nums2[j] < nums1[i]:   j += 1
            else:
                result.append(nums1[i])
                i += 1; j += 1

        return result


# Approach 3: Two pointer, but a bit more pythonic, Time: O(nlog(n)), Space: O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2, result = sorted(nums1), sorted(nums2), []

        while nums1 and nums2:
            top1, top2 = nums1[0], nums2[0]

            if top1 < top2:   nums1.pop(0)
            elif top2 < top1: nums2.pop(0)
            else:
                result.append(top1)
                nums1.pop(0); nums2.pop(0)

        return result


# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Approaches
# Where n is the combined length of both arrays
# Approach 1: Using a hash, Time: O(n) Space: O(n)
# Approach 2: Binary search, iterate through one and sort and do binary search on the other, Time: O(nlog(n)), Space: O(1)
# Approach 3: Two pointer, Time: O(nlog(n)), Space: O(1)

# Follow-up questions
# 1. What if the given array is already sorted? How would you optimize your algorithm?
# 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 3. What if elements of nums2 are stored on disk, and the memory is
#    limited such that you cannot load all elements into the memory at once?

# I think the goal of this question is to test whether the
# interviewee understands some of the data engineering techniques.
# From a data engineer's perspective, basically there are three ideas to solve the question:
# 1. Store the two strings in distributed system (whether self designed or not),
#    then using MapReduce technique to solve the problem;
# 2. Processing the Strings by chunk, which fits the memory,
#    then deal with each chunk of data at a time;
# 3. Processing the Strings by streaming, then check.


# Follow-up and Q & A
# -------------------
# Q. What if the given array is already sorted? How would you optimize your algorithm?
# A. If both arrays are sorted, I would use two pointers to iterate, like merge step in merge sort

# Q. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# A. Suppose lengths of two arrays are N and M,
#    the time complexity of my solution is O(N+M) and the space complexity is O(N) considering the hash.
#    So it's better to use the smaller array to construct the counter hash.
#    Well, as we are calculating the intersection of two arrays,
#    the order of array doesn't matter. We are totally free to swap to arrays.

# Q. What if elements of nums2 are stored on disk,
#    and the memory is limited such that you cannot load all elements into the memory at once?
# A. Divide and conquer. Repeat the process frequently: Slice nums2 to fit into memory,
#    process (calculate intersections), and write partial results to memory.
#    Answer for 3. If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
#    read chunks of array that didn't fit into the memory, and record the intersections.
#    If both nums1 and nums2 are so huge that neither fit into the memory,
#    sort them individually (external sort https://en.wikipedia.org/wiki/External_sorting),
#    then read 2 elements from each array at a time in memory, record intersections.
#    Or stream read them and do two pointer approach
