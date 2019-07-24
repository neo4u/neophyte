class LargerNumKey(str):
    def __lt__(self, x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/