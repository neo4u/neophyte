class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        fin_stack = stack[:-k] if k else stack

        # trip the leading zeros
        return "".join(fin_stack).lstrip('0') or "0"


# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/
