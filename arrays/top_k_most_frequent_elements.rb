# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def top_k_frequent(nums, k)
    map = Hash.new { |hash, key| hash[key] = 0 }

    nums.each do |n|
        map[n] -= 1
    end

    m.sort_by { |key, val| val }.take(k).map(&:first)
end

# Approach 1: Sorting the hash by values and taking k

# Approach 2: Heap
# class Solution:
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """ 
#         count = collections.Counter(nums)   
#         return heapq.nlargest(k, count.keys(), key=count.get)
