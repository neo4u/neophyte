DICT = {
    "2" => "abc", "3" => "def",
    "4" => "ghi", "5" => "jkl", "6" => "mno",
    "7" => "pqrs", "8" => "tuv", "9" => "wxyz"
}

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
    return [] if !digits || digits.empty?
    dfs(digits, 0, "", [])
end

def dfs(digits, idx, path, result)
    if path.size == digits.size
        result.push(path)
        return
    end

    idx.upto(digits.size - 1) do |i|
        DICT[digits[i]].each_char do |c|
            dfs(digits, i + 1, path + c, result)
        end
    end
    result
end

# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Recursive solution (DFS)
# Time complexity O(4 ^ n), where n is length of string [for number 7, recursion tree will have 4 nodes]
# Space complexity O(4 ^ n)

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

