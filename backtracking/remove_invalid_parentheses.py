# Approach 1: Sub-Optimal, Backtracking with pruning Time: O(2^n), Space: O(n)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.n, self.result, self.s = len(s), set(), s
        l, r = self.get_invalid_counts(s)
        if l + r == self.n: return ['']
        self.bt(0, l, r, 0, '')

        return list(self.result)

    def bt(self, i, l_rem, r_rem, balance, path):
        if i == self.n:
            if balance == 0: self.result.add(path)
            return

        if self.s[i] == '(':
            if l_rem: self.bt(i + 1, l_rem - 1, r_rem, balance, path)   # Ignore
            self.bt(i + 1, l_rem, r_rem, balance + 1, path + '(')       # Cosider
        elif self.s[i] == ')':
            if r_rem: self.bt(i + 1, l_rem, r_rem - 1, balance, path)   # Ignore
            if balance: self.bt(i + 1, l_rem, r_rem, balance - 1, path + ')') # Consider
        else:
            self.bt(i + 1, l_rem, r_rem, balance, path + self.s[i])

    def get_invalid_counts(self, s):
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1

        return l, r


# Approach 1:
# 1. We use last_valid_loc, last_remove_loc which start at 0, 0 to keep track of:
#    last_valid_loc: The last ith position brackets were unbalanced.
#    last_remove_loc: The last position at which last bracket was removed.
# 2. We use stack as a counter to see that there are more closing parantheses than open
# 3. If we find that the stack counter is -ve, we recurse removing a close paran char
#    test each char between last_remove_loc to last_valid_loc conditionally
# 4. We do the recursion only if char is a closed paren and one of 2 cases:
#    1. s[j] != s[j - 1]        cuz == can result in duplicates cuz if the previous char
#                               was the same paren type then causing recursive removal can cause a duplicate
#    2. j == last_remove_loc    We're starting from the last j 

# Example Walkthrough
# Input: "())()))()", Output: ["(())()", "()()()"]

# l 
# ())()))()
#   i


# ())()))()
# i: 0, stack: 1
# i: 1, stack: 0
# i: 2, stack: -1
# j: 0, i: 2
# j: 1, i: 2
# s[j - 1] != s[j], last_j: 0, s[j]: ), s[j - 1]: (
#     ()()))()
#     i: 2, stack: 1
#     i: 3, stack: 0
#     i: 4, stack: -1
#     j: 1, i: 4
#     j == last_j, j: 1 last_remove_loc: 1
#     s[j - 1] != s[j], last_j: 1, s[j]: ), s[j - 1]: (
#         (()))()
#         i: 4, stack: -1
#         j: 1, i: 4
#         j: 2, i: 4
#         s[j - 1] != s[j], last_j: 1, s[j]: ), s[j - 1]: (
#             (())()
#             i: 4, stack: 1
#             i: 5, stack: 0
#                 )())((
#                 i: 0, stack: 1
#                 i: 1, stack: 0
#                 i: 2, stack: 1
#                 i: 3, stack: 2
#                 i: 4, stack: 1
#                 i: 5, stack: 0
#                 Reversed string so reverse and append: (())()
#         j: 3, i: 4
#         j: 4, i: 4
#     j: 2, i: 4
#     j: 3, i: 4
#     s[j - 1] != s[j], last_j: 1, s[j]: ), s[j - 1]: (
#         ()())()
#         i: 4, stack: -1
#         j: 3, i: 4
#         j == last_j, j: 3 last_remove_loc: 3
#         s[j - 1] != s[j], last_j: 3, s[j]: ), s[j - 1]: (
#             ()()()
#             i: 4, stack: 1
#             i: 5, stack: 0
#                 )()()(
#                 i: 0, stack: 1
#                 i: 1, stack: 0
#                 i: 2, stack: 1
#                 i: 3, stack: 0
#                 i: 4, stack: 1
#                 i: 5, stack: 0
#                 Reversed string so reverse and append: ()()()
#         j: 4, i: 4
#     j: 4, i: 4
# j: 2, i: 2

# To make the prefix valid, we need to remove a ‘)’.
# The problem is: which one? The answer is any one in the prefix.
# However, if we remove any one, we will generate duplicate results,
# for example: s = ()), we can remove s[1] or s[2] but the result is the same ().
# Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

# After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
# For this, we keep tracking the last removal position and only remove ‘)’ after that.


# Approach 2:
# refer same name file in leetcode_solutions directory
# 1. We use l_rem, r_rem for maintaining "(" and ")" to be removed
# 2. We use l_cnt to track if there is an imbalance of left vs right parans
# 3. if we reached the end of string, we add to result set, if prev_s is valid (l_rem, r_rem, l_cnt == 0)

# Approach without pruning optimizations used above.
# Time Complexity: O(2^N), since in the worst case we will have
#                  only left parentheses in the expression and for every bracket we will have two options
#                  i.e. whether to remove it or consider it. Considering that the expression has N parentheses,
#                  the time complexity will be O(2^N).
# Space Complexity: O(N), because we are resorting to a recursive solution
#                   and for a recursive solution there is always stack space used as
#                   internal function states are saved onto a stack during recursion.
#                   The maximum depth of recursion decides the stack space used.
#                   Since we process one character at a time and the base case for
#                   the recursion is when we have processed all of the characters of the expression string,
#                   the size of the stack would be O(N).
#                   Note that we are not considering the space required to store the valid expressions.
#                   We only count the intermediate space here.

# Approach with pruning optimizations used above.
# Time Complexity: The optimization that we have performed is simply a better form of pruning.
#                  Pruning here is something that will vary from one test case to another.
#                  In the worst case, we can have something like ((((((((( and the left_rem = s.size
#                  and in such a case we can discard all of the characters because all are misplaced.
#                  So, in the worst case we still have 2 options per parenthesis and that gives us a complexity of O(2^N).
# Space Complexity: The space complexity remains the same i.e. O(N) as previous solution.
#                   We have to go to a maximum recursion depth of N before hitting the base case.
#                   Note that we are not considering the space required to store the valid expressions.
#                   We only count the intermediate space here.

# Time: O(2^n), Recursion tree contains 2^n leaf nodes at the final level, increase by power 2 at every level.
# Space: O(n), Stack size can go only upto length of string


# 301. Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/description/


require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(remove_invalid_parentheses_bt('())())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses_bt('()())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses_bt("(a)())()"), ["(a())()", "(a)()()"])
assert_equal(remove_invalid_parentheses_bt(")("), [""])
assert_equal(remove_invalid_parentheses_bt("())"), ["()"])

# assert_equal(remove_invalid_parentheses('())()))()'), ["(())()", "()()()"])
# assert_equal(remove_invalid_parentheses('()())()'), ["(())()", "()()()"])
# assert_equal(remove_invalid_parentheses("(a)())()"), ["(a())()", "(a)()()"])
# assert_equal(remove_invalid_parentheses(")("), [""])
# assert_equal(remove_invalid_parentheses("())"), ["()"])


# ()(()((()