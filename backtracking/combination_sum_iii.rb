# @param {Integer} k
# @param {Integer} n
# @return {Integer[][]}
def combination_sum3(k, n)
    return [] if k.zero? || n.zero?
    nums = (1...10).to_a # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bt(nums, 0, k, [], 0, n, [])
end

def bt(nums, idx, k, path, path_sum, target, result)
    return result.push(path) if path_sum == target && path.size == k

    idx.upto(nums.size - 1) do |i|
        next if path_sum + nums[i] > target
        bt(nums, i + 1, k, path + [nums[i]], path_sum + nums[i], target, result)
    end

    result
end


# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

# Similar problem list
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c++-solution-use-backtracking-easy-understand.

# Points to remember
# 1. No duplicates combinations in result               (So we should consider each unique combination only once)
# 2. Combination can contain a number only once         (This means combination without repitition)
# 3. All numbers are +ve                                (Allows for pruning totals > target)
# 4. The sum must only have k numbers

# Approach 1: Backtracking
# Example: candidates = [2,5,2,1,2], target = 5, expected answer = [ [1,2,2], [5] ]


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(combination_sum3(3, 7), [[1,2,4]])
assert_equal(combination_sum3(3, 9), [[1,2,6], [1,3,5], [2,3,4]])


# **** WITH LOGGING TO SEE RECURSION TREE ***
# def combination_sum2(candidates, target)
#     return [] if !candidates || candidates.empty?
#     # Sorting is to make sure that each output list is sorted to
#     # avoid the repeated combinations in the form like [1 2 3], [3 2 1]
#     candidates.sort!()
#     bt(candidates, 0, [], [], target)
# end

# def bt(candidates, idx, path, result, target, level = -1)
#     level += 1
#     puts "#{"\t" * level}bt call with idx: #{idx} path: #{path} target: #{target} result: #{result}"
#     if target < 0
#         puts "#{"\t" * level}bt retn with idx: #{idx} path: #{path} target: #{target} result: #{result}"
#         return
#     end
#     if target == 0
#         puts "#{"\t" * level}bt retn with idx: #{idx} path: #{path} target: #{target} result: #{result}"
#         return result.push(path)
#     end

#     idx.upto(candidates.size - 1) do |i|
#         puts "#{"\t" * level}checking next candidate for use or prune idx: #{i}, candidate: #{candidates[i]}"
#         next if i != idx && candidates[i] == candidates[i - 1]                                  # Skip duplicates, after i crosses idx
#         break if nums[i] > target
#         bt(candidates, i + 1, path + [candidates[i]], result, target - candidates[i], level)    # Check for solutions for target - curr number,
#                                                                                                 # Use i + 1 as start index for next level, to avoid repition in combination
#     end
#     puts "#{"\t" * level}bt retn with idx: #{idx} path: #{path} target: #{target} result: #{result}"

#     result
# end
