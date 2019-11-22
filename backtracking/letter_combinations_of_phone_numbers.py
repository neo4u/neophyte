from typing import List


MAP = {
    "2": "abc", "3": "def",
    "4": "ghi", "5": "jkl", "6": "mno",
    "7": "pqrs", "8": "tuv", "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.combos = []
        self.bt(digits, 0, "")
        return self.combos

    def bt(self, digits, i, path):
        if len(path) == len(digits): return self.combos.append(path)

        for c in MAP[digits[i]]:
            self.bt(digits, i + 1, path + c)


# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


sol = Solution()
assert sol.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


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
