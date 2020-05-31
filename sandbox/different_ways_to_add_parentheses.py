from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def diffWaysToCompute(self, s: str) -> List[int]:
        level_results, ops = [], ['+', '-', '*']
        if s in self.cache: return self.cache[s]

        for i, c in enumerate(s):
            if c not in ops: continue
            l, r = s[:i], s[i + 1:]
            l_results, r_results = self.diffWaysToCompute(l), self.diffWaysToCompute(r)
            # Same as below, don't let that confuse u, just the pythonic way
            for d1 in l_results:
                for d2 in r_results:
                    level_results.append(self.do_op(d1, d2, c))

        if not level_results: level_results.append(int(s))
        self.cache[s] = level_results

        return level_results

    def do_op(self, m, n, op):
        if op == "+":   return m + n
        elif op == "-": return m - n
        elif op == '*': return m * n

# 241. Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/


# 1. Iterate through characters, and skip operands
# 2. When we hit an operator, get left operand and right operand and recurive get their results
# 3. Then use left and right results to generate every combination and combine them using the curr operator
# 4. If we don't get any results at the current level, then just return the int value of the current string,
#    bcuz the string must be an int
