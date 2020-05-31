from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # majority voting
        ele1, ele2 = 0, 0
        cnt1, cnt2 = 0, 0
        n = len(nums)

        # using majority vote to find two most popular elements
        for num in nums:
            if ele1 == num:
                cnt1 += 1
            elif ele2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = num
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == ele1:     cnt1 += 1
            elif num == ele2:   cnt2 += 1

        out = []
        if cnt1 > n//3: out.append(ele1)
        if cnt2 > n//3: out.append(ele2)
        return out




# majority vote -- python -- O(1) Space -- O(N) time

# The idea is first to loop over nums to identify the most populart two elements using O(N) time,
# and then loop over the array again to check if the majority element is the right one
# we are looking for with condition of count>len(nums)/3.
