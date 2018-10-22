# Approach 2: Optimal, Backtracking with pruning Time: O(2^n), Space: O(n)
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    @str, @result = String.new(s), Set.new() # Set to avoid duplicates, because removing same number of diff parentheses, can lead to same result
    l, r = get_counts(@str)

    return [""] if l + r == @str.size
    backtrack(0, l, r, 0, "")

    @result.to_a
end

def backtrack(i, l_rem, r_rem, left_count, prev)
    # If we reached the end of the string, just check if the resulting expression is
    # valid or not and also if we have removed the total number of left and right
    # parentheses that we should have removed.
    if i == @str.size
        @result.add(prev) if left_count == 0 && l_rem.zero? && r_rem.zero?
        return
    end

    # The discard case. Note that here we have our pruning condition.
    # We don't recurse if the remaining count for that parenthesis is == 0.
    if @str[i] == "("
        backtrack(i + 1, l_rem - 1, r_rem, left_count, prev) if l_rem > 0  # The discard case, it will work without the if condition, which is for pruning/optimization
        backtrack(i + 1, l_rem, r_rem, left_count + 1, prev + "(")         # The consider case
    elsif @str[i] == ")"
        backtrack(i + 1, l_rem, r_rem - 1, left_count, prev) if r_rem > 0              # The discard case, it will work without the if, which is for pruning
        backtrack(i + 1, l_rem, r_rem, left_count - 1, prev + ")") if left_count > 0   # The consider case, but only when more left than right
    else
        backtrack(i + 1, l_rem, r_rem, left_count, prev + @str[i])
    end
end

def get_counts(s)
    l, r = 0, 0
    s.each_char do |c|
        l += c == "(" ? 1 : 0

        if l == 0
            r += c == ")" ? 1 : 0 # If we don't have a matching left, then this is a misplaced right, record it.
        else
            l -= c == ")" ? 1 : 0 # Decrement count of left parentheses because we have found a right which CAN be a matching one for a left.
        end
    end
    [l, r]
end

# Approach 1: Using valid? to check counts each time. Almost optimal. As same pruning in 
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses_using_valid(s)
    l, r = get_counts(s)
    @result = []
    dfs(s, 0, l, r)

    @result
end

def get_counts(s)
    l, r = 0, 0
    s.each_char do |c|
        l += c == "(" ? 1 : 0

        if l == 0
            r += c == ")" ? 1 : 0 # If we don't have a matching left, then this is a misplaced right, record it.
        else
            l -= c == ")" ? 1 : 0 # Decrement count of left parentheses because we have found a right which CAN be a matching one for a left.
        end
    end
    [l, r]
end

def valid?(s)
    cnt = 0
    s.each_char do |c|
        if c == "(" then cnt += 1
        elsif c == ")" then cnt -= 1 end
        return false if cnt < 0
    end

    true
end

def dfs(s, start, l, r)
    if l == 0 && r == 0 && valid?(s)
        @result.push(s)
        return
    end

    n = s.size
    start.upto(n - 1) do |i|
        next if i > start && s[i] == s[i - 1] # we restrict ourself to remove the first )
        cur = s[0...i] + s[i + 1...n]

        if r > 0 && s[i] == ")"
            dfs(cur, i, l, r - 1)
        elsif l > 0 && s[i] == "("
            dfs(cur, i, l - 1, r)
        end
    end
end

# time complexity: T(n) = n^2 * T(n-1). One point is : valid is only called at the bottom of recursion tree.
# T(n)=n^2 * (n-1)^2 * (n-2)^2 ...2^2 * n1 = n(n!)^2

# Explanation Approach 1:
# We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
# The counter will increase when it is ‘(‘ and decrease when it is ‘)’.
# Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

# To make the prefix valid, we need to remove a ‘)’.
# The problem is: which one? The answer is any one in the prefix.
# However, if we remove any one, we will generate duplicate results,
# for example: s = ()), we can remove s[1] or s[2] but the result is the same ().
# Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

# After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
# For this, we keep tracking the last removal position and only remove ‘)’ after that.

# refer same name file in leetcode_solutions directory
# 1. We use l_rem, r_rem for maintaining "(" and ")" to be removed
# 2. We use left_count to track if there is an imbalance of left vs right parans
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

# Time: O(2^n)
# Space: O(n)

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(remove_invalid_parentheses('())())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses('()())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses("(a)())()"), ["(a())()", "(a)()()"])
assert_equal(remove_invalid_parentheses(")("), [""])
assert_equal(remove_invalid_parentheses("())"), ["()"])

assert_equal(remove_invalid_parentheses_using_valid('())())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses_using_valid('()())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses_using_valid("(a)())()"), ["(a())()", "(a)()()"])
assert_equal(remove_invalid_parentheses_using_valid(")("), [""])
assert_equal(remove_invalid_parentheses_using_valid("())"), ["()"])
