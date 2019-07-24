# @param {String} digits
# @return {String[]}
MAP = {
    "2" => "abc", "3" => "def",
    "4" => "ghi", "5" => "jkl", "6" => "mno",
    "7" => "pqrs", "8" => "tuv", "9" => "wxyz"
}

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
    return [] if !digits || digits.empty?
    bt(digits, 0, "", [])
end

def bt(digits, index, path, result)
    return result.push(path) if path.size == digits.size

    MAP[digits[index]].each_char do |c|
        bt(digits, index + 1, path + c, result)
    end

    result
end

# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


# BT Funciton for troubleshooting and print of recursion tree
# def bt(digits, index, path, result, level = -1)
#     level += 1
#     puts "#{"\t" * level}bt call with index: #{index} path: #{path} result: #{result.inspect}"
#     if path.size == digits.size
#         result.push(path)
#         return
#     end

#     index.upto(digits.size - 1) do |i|
#         puts "#{"\t" * level}i: #{i}"
#         MAP[digits[i]].each_char do |c|
#             bt(digits, i + 1, path + c, result, level)
#         end
#     end
#     puts "#{"\t" * level}bt retn with index: #{index} path: #{path} result: #{result.inspect}"

#     result
# end

