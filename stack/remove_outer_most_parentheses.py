class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result, opened = [], 0

        for c in S:
            if c == '(' and opened > 0: result.append(c)
            if c == ')' and opened > 1: result.append(c)
            opened += 1 if c == '(' else -1

        return "".join(result)


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        list_s = list(S)
        i, n = 0, len(S)
        stack, outer_start = [], 0

        while i < n:
            if list_s[i] == '(':    stack.append('(')
            else:                   stack.pop()

            if not stack:
                outer_end = i
                list_s[outer_start], list_s[outer_end] = '', ''
                outer_start = i + 1
            i += 1

        return ''.join(list_s)

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack, result = [], ""

        for c in S:
            if c == "(":
                if stack: result += c   # that means, the current "(" is not an outermost bracket
                stack.append(c)         # push the current "(" in stack
            else:                       # if closing bracket appears
                stack.pop()             # pop the respective opening bracket from stack
                if stack:               # if the opening bracket was not the last value in the stack
                    result += c         # then append it to the result string.

        return result



# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/description/

# Example 1:

# Intuition:
# - We need to remove outer parentheses of every primitive group (Valid by itself, and can't be broken down further)
# - Stack comes to mind, however, a counter of parentheses is even better

# Approach 1: With Stack, O(n) space
        # We use stack data structure to keep a track of opening and closing brackets.
        # We have a result string in which we will apppend all the brackets other than
        # the outer brackets.

        # Outer most parentheses would mean that the opening brackets would be
        # at the bottom of the stack. We do not have to consider stack's bottom most
        # bracket in the result string.


# Approach 2: With Counter, O(1) space
# Steps:
# 1. for each char c in string s, we check open or close, we increment or decrement 'opened'
# 2. if c is open char, and opened is > 0, this means a valid group has started, so we can add c to result
# 3. if c is close char, and opened is > 1, this means this close will address an open,
#    but there are still opens left to be matched, hence it indicates an ongoing primitive group
# 4. We return the string formed by result


# Time: O(n)
# Space: O(1)