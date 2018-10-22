# @param {String} s
# @return {Boolean}
def is_valid(s)
    stack = []
    
    s.each_char do |c|
        if c == '(' then stack.push(')')    # open case
        elsif c == '{' then stack.push('}') # open case
        elsif c == '[' then stack.push(']') # open case
        elsif stack.empty? || stack.pop() != c then return false end # close case so check for match
    end

    stack.empty?
end

# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/submissions/

# Push the corresponding closing brace onto stack each time we get an opening brace
# Each time we get a closing brace check match with top of stack and return false if not a match

# Time: O(n)
# Space: O(1)