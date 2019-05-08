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
    if path.size == digits.size
        result.push(path)
        return
    end

    MAP[digits[index]].each_char do |c|
        bt(digits, index + 1, path + c, result)
    end

    result
end

# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# bt call with index: 0 path:  result: []
# i: 0
#     bt call with index: 1 path: a result: []
#     i: 1
#         bt call with index: 2 path: ad result: []
#         bt call with index: 2 path: ae result: ["ad"]
#         bt call with index: 2 path: af result: ["ad", "ae"]
#     bt retn with index: 1 path: a result: ["ad", "ae", "af"]
#     bt call with index: 1 path: b result: ["ad", "ae", "af"]
#     i: 1
#         bt call with index: 2 path: bd result: ["ad", "ae", "af"]
#         bt call with index: 2 path: be result: ["ad", "ae", "af", "bd"]
#         bt call with index: 2 path: bf result: ["ad", "ae", "af", "bd", "be"]
#     bt retn with index: 1 path: b result: ["ad", "ae", "af", "bd", "be", "bf"]
#     bt call with index: 1 path: c result: ["ad", "ae", "af", "bd", "be", "bf"]
#     i: 1
#         bt call with index: 2 path: cd result: ["ad", "ae", "af", "bd", "be", "bf"]
#         bt call with index: 2 path: ce result: ["ad", "ae", "af", "bd", "be", "bf", "cd"]
#         bt call with index: 2 path: cf result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce"]
#     bt retn with index: 1 path: c result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# i: 1
#     bt call with index: 2 path: d result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#     bt retn with index: 2 path: d result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#     bt call with index: 2 path: e result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#     bt retn with index: 2 path: e result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#     bt call with index: 2 path: f result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#     bt retn with index: 2 path: f result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# bt retn with index: 0 path:  result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

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