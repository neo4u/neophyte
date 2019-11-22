class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'{': '}', '(': ')', '[': ']'}
        stack = []

        for c in s:
            if c in parens: stack.append(parens[c])
            else:
                if not stack or stack.pop() != c: return False

        return stack == []


# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/submissions/

# Push the corresponding closing brace onto stack each time we get an opening brace
# Each time we get a closing brace check match with top of stack and return false if not a match

# Time: O(n)
# Space: O(1)