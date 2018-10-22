# @param {Integer} n
# @return {String[]}
def generate_parenthesis(n)
    def backtrack(n, s = '', l = 0, r = 0, result = [])
        puts s
        puts "l: #{l}, r: #{r}"
        if s.size == 2 * n
            result.push(s)
            return result
        end
    
        backtrack(n, s + "(", l + 1, r, result) if l < n
        backtrack(n, s + ")", l, r + 1, result) if r < l
    
        result
    end

    backtrack(n)
end

# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

# Complexity Analysis
# Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n).
# This analysis is outside the scope of this article, 
# but it turns out this is the n-th Catalan number 1/ (n + 1) * (2nCn), which is bounded asymptotically by 4^n / n * sqrt(n).

# Time Complexity: O(4^n/sqrt(n), Each valid sequence has at most n steps during the backtracking procedure.
# Space Complexity: O(4^n/sqrt(n), as described above, and using O(n) space to store the sequence.

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(generate_parenthesis(3), [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
])
