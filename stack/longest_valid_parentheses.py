# Approach 3: Stack, Space: O(n)
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        stack, max_len = [-1], 0

        for i, c in enumerate(s):
            if c == '(': stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: max_len = max(max_len, i - stack[-1])

        return max_len


# Approach 3: l, r counters, Space: O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r, max_len = 0, 0, 0

        for c in s:
            if c == '(':    l += 1
            else:           r += 1

            if l == r:  max_len = max(max_len, l + r)
            elif r > l: l = r = 0

        l, r = 0, 0
        for c in reversed(s):
            if c == '(':    l += 1
            else:           r += 1

            if l == r:  max_len = max(max_len, l + r)
            elif l > r: l = r = 0

        return max_len


# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/description/

# Approach 1: Brute Force

# Approach 2: DP

# Approach 3: Stack
# Steps:
# 1. We use a stack and push -1 to indicate the index for our math.
# 2. For every (, we push its index onto the stack.
# 3. For every ), we pop and do i - stack[-1] to get len and update max_len if better.
# 4. If the stack becomes empty at any point while popping,
#    we push the current index onto the stack, again for our math.
# 5. Since our max_len keeps track of the running max, we return it at the end.

# Example 1: s = '(()'
# stack = []
# i, c = 0, (
# push 0, stack = [-1, 0]
# i, c = 1, (
# push 1, stack = [-1, 0, 1]
# i, c = 2, )
# pop 1, and take r - l = 2 - 0 == 2
# return 2

# Example 2: s = )()())
# stack = [-1], max_len = 0

# i, c = 0, )
# pop -1, stack = [0]
# i, c = 1, (
# push 1, stack = [1]
# i, c = 2, )
# pop 1, stack = [0]
# and take max_len = max(0, r - l) = 2 - 0 == 2
# i, c = 3, (
# push 3, stack = [0, 3]
# i, c = 4, )
# pop 3, stack = [0]
# and take max_len = max(0, r - l) = 4 - 0 == 4
# i, c = 5, )
# pop 0
# return 4

# Example 3: s = )))())
# Note how we keep the stack honest by append the curr i everytime, it gets empty
# stack = [-1], max_len = 0

# i, c = 0, )
# pop -1, push 0, stack = [0]
# i, c = 1, )
# pop 0, push 1 stack = [1]
# i, c = 2, )
# pop 1, push 2, stack = [2]
# and take max_len = max(0, r - l) = 2 - 0 == 2
# i, c = 3, (
# push 3, stack = [2, 3]
# i, c = 4, )
# pop 3, stack = [2]
# and take max_len = max(0, r - l) = 2 - 0 == 2
# i, c = 5, )
# pop 0
# return 2

# Time: O(n)
# Space: O(n)

# Approach 4: Two Pass using l, r counters and scanning from front and back
# Steps:
# 1. 1st pas


# Example 1: s = '(()'
# l, r = 0, 0
# c = (
# l, r = 1, 0

# c = (
# l, r = 2, 0

# c = )
# l, r = 0, 0


# return 2

# Example 2: s = )()())
# 1st pass
# l, r = 0, 0
# c = )
# r > l: so reset l, r = 0, 0
# c = (
# l, r = 1, 0

# c = )
# l, r = 1, 1
# record max_len = 2

# c = (
# l, r = 2, 1

# c = )
# l, r = 2, 2
# record max_len = 4

# c = )
# l, r = 2, 3
# reset l, r = 0, 0

# 2nd pass reversed = '))()()'
# l, r = 0, 0
# c = )
# l, r = 0, 1

# c = )
# l, r = 0, 2

# c = (
# l, r = 1, 2

# c = )
# l, r = 1, 3

# c = (
# l, r = 2, 3
# record max_len = 4

# c = )
# l, r = 2, 4
# We never reach a state to do a record of max_len or reset of l, r = 0, 0
# Because we never hit the conditions of l > r or l == r
# so we return 4

# Example 3: s = )))())
# 1ST PASS
# l, r = 0, 0

# c = )
# l, r = 0, 1
# r > l: so reset l, r = 0, 0

# c = )
# l, r = 0, 1
# r > l: so reset l, r = 0, 0

# c = )
# l, r = 0, 1
# r > l: so reset l, r = 0, 0

# c = (
# l, r = 1, 0

# c = )
# l, r = 1, 1
# record max_len = 2

# c = )
# l, r = 1, 2
# r > l: so reset l, r = 0, 0

# 2ND PASS: reversed = ))()))
# l, r = 0, 0

# c = )
# l, r = 0, 1

# c = )
# l, r = 0, 2

# c = (
# l, r = 1, 2

# c = )
# l, r = 1, 3

# c = )
# l, r = 1, 4

# c = )
# l, r = 1, 5
# We never reach a state to do a record of max_len or reset of l, r = 0, 0
# Because we never hit the conditions of l > r or l == r
# so we return 2



# Time: O(n)
# Space: O(1)

sol = Solution1()
assert sol.longestValidParentheses('(()') == 2
assert sol.longestValidParentheses(')()())') == 4
assert sol.longestValidParentheses(')))())') == 2

sol = Solution()
assert sol.longestValidParentheses('(()') == 2
assert sol.longestValidParentheses(')()())') == 4
assert sol.longestValidParentheses(')))())') == 2
