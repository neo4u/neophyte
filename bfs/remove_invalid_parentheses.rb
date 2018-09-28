# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    return [''] if !s || s.empty?
    result, visited, q, exit_level = [], Set.new([s]), [s], false

    while !q.empty?
        curr = q.shift()

        if valid?(curr)
            result.push(curr)
            exit_level = true
        end
        # If answer is found, make exit_level true so that only this level's valid strings are processed.
        # Essentially no more strings are added to the q.
        next if exit_level

        # For each paranthesis char we try to remove it and check validity through the Q. if not already checked.
        0.upto(curr.size - 1) do |i|
            next if !['(', ')'].include?(curr[i])
            next_str = curr[0...i] + curr[i + 1...curr.size]
            next if visited.include?(next_str)
            q.push(next_str)
            visited.add(next_str)
        end
    end

    result
end

def valid?(s)
    count, n = 0, s.size
    0.upto(n - 1) do |i|
        if s[i] == '('
            count += 1
        elsif s[i] == ')'
            count -= 1
        end
        return false if count < 0
    end

    count == 0
end

# On the first level, there's only one string which is the input string s, let's say the length of it is n, to check whether it's valid, we need O(n) time.
# On the second level, we remove one ( or ) from the first level, so there are C(n, n-1) new strings, each of them has n-1 characters, and for each string,
# we need to check whether it's valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1).
# Come to the third level, total time complexity is (n-2) x C(n, n-2), so on and so forth...

# Finally we have this formula:

# T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).


# T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).

require 'set'
require 'test/unit'
extend Test::Unit::Assertions

assert_equal(remove_invalid_parentheses('()())()'), ["(())()", "()()()"])
assert_equal(remove_invalid_parentheses("(a)())()"), ["(a())()", "(a)()()"])
assert_equal(remove_invalid_parentheses(")("), [""])
