from typing import List




# Approach 2: TreeSet Java or Custom BST in python
# public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
#     TreeSet<Integer> set = new TreeSet<>();

#     for (int i = 0; i < nums.length; ++i) {
#         // Find the successor of current element
#         Integer s = set.ceiling(nums[i]);
#         if (s != null && s <= nums[i] + t) return true;

#         // Find the predecessor of current element
#         Integer g = set.floor(nums[i]);
#         if (g != null && nums[i] <= g + t) return true;

#         set.add(nums[i]);
#         if (set.size() > k) {
#             set.remove(nums[i - k]);
#         }
#     }
#     return false;
# }

# Time: O(n * log(min(n, k))
# Space: O(min(n, k))

# Approach 3: Method using buckets
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        n, d, w = len(nums), {}, t + 1

        for i in range(n):
            m = nums[i] // w                                            # Find the bucket this falls in
            if m in d: return True                                      # Each bucket must contain at most one element
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w: return True  # Check the neighbor buckets for almost duplicate
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w: return True

            d[m] = nums[i]                                              # At this point bucket m is empty and no almost duplicate in neighbor buckets
            if i >= k: d.pop(nums[i - k] // w)                          # Once i crosses k, we keep removing each element outside the k window

        return False



# 220. Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/description/


# Approach 2: TreeSet Java or Custom BST in python

# Time: O(n * log(min(n, k))
# Space: O(min(n, k))

# Approach 3: Method using buckets

# Intuition:
# - Visualize if you want someone with 30 days of b'day from you,
#   we immediately eliminate, people with b'days all months except +1 and -1 month from you
# - this is the concept of buckets
# - We use this with bucket size 2t

# Steps:
# 

# Time: O(n)
# Space: O(min(n, k))

sol = Solution()
assert sol.contains_nearby_almost_duplicate([-1, -1], 1, 0) == True
assert sol.contains_nearby_almost_duplicate([2, 1], 1, 1) == True
assert sol.contains_nearby_almost_duplicate([-1, -1], 1, -1) == False
