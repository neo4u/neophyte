class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = str(num)
        n, digits = len(str_num), list(map(int, str_num))
        buckets = {}
        for i, x in enumerate(digits):
            buckets[x] = i

        for i in range(n):
            for k in range(9, digits[i], -1):
                if k not in buckets or buckets[k] <= i: continue
                digits[i], digits[buckets[k]] = digits[buckets[k]], digits[i]
                return int(''.join(map(str, digits)))

        return num


class Solution:
    def maximumSwap(self, A: int) -> int:
        A = map(int, str(A))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return A

# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap/description/


# Approach 1: Greedy

# Intuition

# At each digit of the input number in order, if there is a larger digit that occurs later, we know that the best swap must occur with the digit we are currently considering.

# Algorithm

# We will compute \text{last[d] = i}last[d] = i, the index \text{i}i of the last occurrence of digit \text{d}d (if it exists).

# Afterwards, when scanning the number from left to right, if there is a larger digit in the future, we will swap it with the largest such digit; if there are multiple such digits, we will swap it with the one that occurs the latest.


# Time: O(n)
# Space: O(1)