class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        sign = '-' if num * den < 0 else ''
        head, rem = divmod(abs(num), abs(den))
        tail, seen = '', {}

        while rem != 0:
            if rem in seen:
                i = seen[rem]
                non_recur, recur = tail[:i], '(' + tail[i:] + ')'
                tail = non_recur + recur
                break

            seen[rem] = len(tail)
            next_digit, rem = divmod(rem * 10, abs(den))
            tail += str(next_digit)

        return sign + str(head) + (tail and '.' + tail)


# 166. Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/

# Steps:


sol = Solution()

assert sol.fractionToDecimal(1, 2) == '0.5'
assert sol.fractionToDecimal(2, 1) == '2'
assert sol.fractionToDecimal(2, 3) == '0.(6)'
