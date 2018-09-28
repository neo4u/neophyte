
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    rm_l, rm_r, @result = 0, 0, []

    s.each_char do |c|
        rm_l += c == "(" ? 1 : 0

        if rm_l == 0
            rm_r += c == ")" ? 1 : 0
        else
            rm_l -= c == ")" ? 1 : 0
        end
    end
    puts "s is #{s}"
    puts "rm_l: #{rm_l} and rm_r: #{rm_r}"
    dfs(s, 0, rm_l, rm_r)
    puts
    @result
end

def valid?(s)
    stack = 0
    s.each_char do |c|
        if c == "(" then stack += 1
        elsif c == ")" then stack -= 1 end
        return false if stack < 0
    end

    true
end

def dfs(s, start, rm_l, rm_r)
    puts "DFS called with: #{s} | start: #{start} | rm_l: #{rm_l} | rm_r: #{rm_r}"
    n = s.size
    if rm_l == 0 && rm_r == 0 && valid?(s)
        @result.push(s)
        puts "#{s} is valid"
        puts 'Returning'
        return
    end

    start.upto(n - 1) do |i|
        # This line is critical because it avoid duplicates in situations like ()) we only need to remove the first )
        next if i > start && s[i] == s[i - 1]
        cur = s[0...i] + s[i + 1...n]
        puts "cur is #{cur}"

        
        # When the ith char is ) and we have more right parenthees to remove (rm_r) dfs from the ith char to end with rm_r - 1
        if rm_r > 0 && s[i] == ")"
            dfs(cur, i, rm_l, rm_r - 1)
        # When the ith char is ) and we have more left parenthees to remove (rm_r) dfs from the ith char to end with rm_l - 1
    elsif rm_l > 0 && s[i] == "("
            dfs(cur, i, rm_l - 1, rm_r)
        end
    end
end

# time complexity: T(n) = n^2 * T(n-1). One point is : valid is only called at the bottom of recursion tree.
# T(n)=n^2 * (n-1)^2 * (n-2)^2 ...2^2 * n1 = n(n!)^2

# Explanation:
# We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
# The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.

# To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

# After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order.
# For this, we keep tracking the last removal position and only remove ‘)’ after that.


require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(remove_invalid_parentheses('())())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses('()())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses("(a)())()"), ["(a())()", "(a)()()"])
assert_equal(remove_invalid_parentheses(")("), [""])
assert_equal(remove_invalid_parentheses("())"), ["()"])