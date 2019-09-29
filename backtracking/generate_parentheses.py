from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.bt(n, 0, 0, "")
        return self.result

    def bt(self, n: int, l: int, r: int, path: str) -> None:
        if len(path) == 2 * n: return self.result.append(path)

        if l < n: self.bt(n, l + 1, r, path + "(")
        if r < l: self.bt(n, l, r + 1, path + ")")


# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

# Complexity Analysis
# Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n).
# This analysis is outside the scope of this article,
# but it turns out this is the n-th Catalan number 1/ (n + 1) * (2nCn), which is bounded asymptotically by 4^n / n * sqrt(n).

# Time: O(4^n/sqrt(n), Each valid sequence has at most n steps during the backtracking procedure.
# Space: O(4^n/sqrt(n), as described above, and using O(n) space to store the sequence.


# n = 2

# bt("", 0, 0)
#     bt("(", 1, 0)
#         bt("((", 2, 0)
#             can't open
#             ret
#         bt('(()', 2, 1)
#             bt('(())', 2, 2)
#             can't open can't close
#             ret
#         ret
#         bt('()', 1, 1)
#             bt('()(', 2, 1)
#                 bt('()()', 2, 2)
#                 ret
#             ret
#         ret

# *** Example: n = 3 *** Space after each DFS instance
# backtrack called with  "" 0 0 []
#   backtrack called with ( 1 0 []
#     backtrack called with (( 2 0 []
#       backtrack called with ((( 3 0 []
#         backtrack called with ((() 3 1 []
#           backtrack called with ((()) 3 2 []
#             backtrack called with ((())) 3 3 []
#           backtrack return with ((()) 3 2 ["((()))"]
#         backtrack return with ((() 3 1 ["((()))"]
#       backtrack return with ((( 3 0 ["((()))"]
#       backtrack called with (() 2 1 ["((()))"]
#         backtrack called with (()( 3 1 ["((()))"]
#           backtrack called with (()() 3 2 ["((()))"]
#             backtrack called with (()()) 3 3 ["((()))"]
#           backtrack return with (()() 3 2 ["((()))", "(()())"]
#         backtrack return with (()( 3 1 ["((()))", "(()())"]
#         backtrack called with (()) 2 2 ["((()))", "(()())"]
#           backtrack called with (())( 3 2 ["((()))", "(()())"]
#             backtrack called with (())() 3 3 ["((()))", "(()())"]
#           backtrack return with (())( 3 2 ["((()))", "(()())", "(())()"]
#         backtrack return with (()) 2 2 ["((()))", "(()())", "(())()"]
#       backtrack return with (() 2 1 ["((()))", "(()())", "(())()"]
#     backtrack return with (( 2 0 ["((()))", "(()())", "(())()"]
#     backtrack called with () 1 1 ["((()))", "(()())", "(())()"]
#       backtrack called with ()( 2 1 ["((()))", "(()())", "(())()"]
#         backtrack called with ()(( 3 1 ["((()))", "(()())", "(())()"]
#           backtrack called with ()(() 3 2 ["((()))", "(()())", "(())()"]
#             backtrack called with ()(()) 3 3 ["((()))", "(()())", "(())()"]
#           backtrack return with ()(() 3 2 ["((()))", "(()())", "(())()", "()(())"]
#         backtrack return with ()(( 3 1 ["((()))", "(()())", "(())()", "()(())"]
#         backtrack called with ()() 2 2 ["((()))", "(()())", "(())()", "()(())"]
#           backtrack called with ()()( 3 2 ["((()))", "(()())", "(())()", "()(())"]
#             backtrack called with ()()() 3 3 ["((()))", "(()())", "(())()", "()(())"]
#           backtrack return with ()()( 3 2 ["((()))", "(()())", "(())()", "()(())", "()()()"]
#         backtrack return with ()() 2 2 ["((()))", "(()())", "(())()", "()(())", "()()()"]
#       backtrack return with ()( 2 1 ["((()))", "(()())", "(())()", "()(())", "()()()"]
#     backtrack return with () 1 1 ["((()))", "(()())", "(())()", "()(())", "()()()"]
#   backtrack return with ( 1 0 ["((()))", "(()())", "(())()", "()(())", "()()()"]
# backtrack return with  0 0 ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Refer to the attached diagram for recursion,
# The numbers next to each node are the counts of left and right parantheses

sol = Solution()
assert sol.generateParenthesis(3) == [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
assert sol.generateParenthesis(2) == [
    "(())",
    "()()"
]
