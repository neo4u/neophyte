class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_set = set()
        for num in nums:
            if num in n_set: return True
            n_set.add(num)

        return False


# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/


sol = Solution()

assert sol.containsDuplicate([1, 2, 3, 1]) == True
assert sol.containsDuplicate([1, 2, 3, 4]) == False
assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
