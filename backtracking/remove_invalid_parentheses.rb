# Approach 1: Sub-Optimal, Backtracking with pruning Time: O(2^n), Space: O(n)
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses_bt(s)
    # Set to avoid duplicates, because removing same number of diff parentheses, can lead to same result
    @str, @result = s, Set.new()
    l, r = get_invalid_counts(@str)

    return [""] if l + r == @str.size
    backtrack(0, l, r, 0, "")

    @result.to_a
end

def backtrack(i, l_rem, r_rem, l_cnt, prefix, depth = 0)
    # If we reached the end of the string, just check if the resulting expression is
    # valid or not and also if we have removed the total number of left and right
    # parentheses that we should have removed.
    if i == @str.size
        @result.add(prefix) if l_cnt == 0 && l_rem.zero? && r_rem.zero?
        return
    end

    # The discard case. Note that here we have our pruning condition.
    # We don't recurse if the remaining count for that parenthesis is == 0.
    if @str[i] == "("
        backtrack(i + 1, l_rem - 1, r_rem, l_cnt, prefix) if l_rem > 0      # The discard case, it will work without the if condition, which is for pruning/optimization
        backtrack(i + 1, l_rem, r_rem, l_cnt + 1, prefix + "(", depth + 1)  # The consider case
    elsif @str[i] == ")"
        backtrack(i + 1, l_rem, r_rem - 1, l_cnt, prefix) if r_rem > 0        # The discard case, it will work without the if, which is for pruning
        backtrack(i + 1, l_rem, r_rem, l_cnt - 1, prefix + ")", depth + 1) if l_cnt > 0  # The consider case, but only when more left than right
    else
        backtrack(i + 1, l_rem, r_rem, l_cnt, prefix + @str[i])
    end
end

def get_invalid_counts(s)
    l, r = 0, 0

    s.each_char do |c|
        if c == '('
            l += 1
        elsif c == ')'
            if l == 0   # If we don't have a matching left, then this is a misplaced right, record it.
                r += 1
            else
                l -= 1  # Decrement count of left parentheses because we have found a right which CAN be a matching one for a left.
            end
        end
    end

    [l, r]
end


# Best solution
def remove_invalid_parentheses(s)
    @result, parens  = [], ['(', ')']
    remove(s, 0, 0, parens)
    @result
end

# To keep track of:

def remove(s, last_valid_loc, last_remove_loc, parens)
    stack = 0
    open, close = parens[0], parens[1]
    last_valid_loc.upto(s.size - 1) do |i|
        stack += 1 if s[i] == open
        stack -= 1 if s[i] == close
        next if stack >= 0
        # s is not valid, try removing every possible closeParen, skipping duplicates

        # normally we should use i + 1 and j + 1 as next starting location
        # but after deleting one char, i and j are effectivelly increased by 1 already
        last_remove_loc.upto(i) do |j|
            if s[j] == close && (j == last_remove_loc || s[j - 1] != s[j])
                remove(s[0...j] + s[j + 1..-1], i, j, parens)
            end
        end
        return # whenever was is invalid, the child of recursive pushes valid sub string into the result, so return as nothing to after this
    end
    #  if we reach here, current s is valid without any fix.
    #  But each s should go through two pass, the second pass is for reversed string.
    #  so we need to check if this is the first pass, if yes, reverse s and check again
    #  if this is second pass, just save result
    #  how to check if it's first pass? use the order of open/close Parentheses as flag
    if open == '('
        remove(s.reverse, 0, 0, [')', '('])
    else
        @result << s.reverse
    end
end

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