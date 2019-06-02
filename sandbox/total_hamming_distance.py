class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        counts = [0] * 32

        for num in nums:
            i = 0

            while num:
                counts[i] += num & 1
                num >>= 1
                i += 1

        for k in counts:
            result += k * (n - k)  # k C 1 * (n - k) C 1 (Ways of combining 1 element from 2 sets of sets bits and unset bits)

        return result


class Solution(object):
    def totalHammingDistance(self, nums):
        xmap = map("{:032b}".format, nums)
        total, n = 0, len(nums)

        for i in zip(*xmap):
            k = i.count('1')
            total += k * (n - k)

        return total