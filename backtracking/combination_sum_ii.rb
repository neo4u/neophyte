# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum2(candidates, target)
    return [] if !candidates || candidates.empty?
    @result = []
    # Sorting is to avoid the repeated combinations in the form like [1 2 3], [3 2 1]
    candidates.sort!()
    bt(candidates, 0, [], target)

    @result
end

def bt(nums, idx, path, target)
    return @result.push(path) if target == 0                         # Base case: if path sum == target, it as a solution so push & return

    idx.upto(nums.size - 1) do |i|
        break if nums[i] > target
        next if i != idx && nums[i] == nums[i - 1]                  # Skip duplicates, after i crosses idx
        bt(nums, i + 1, path + [nums[i]], target - nums[i]) # Check for solutions for target - curr number,
                                                                    # Use i + 1 as start index for next level, to avoid repition in combination
    end
end


# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/

# Similar problem list
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c++-solution-use-backtracking-easy-understand.

# Points to remember
# 1. No duplicates combinations in result               (So we should consider each unique combination only once)
# 2. Can't pick same element twice Combination can contain a number only once         (This means combination without repitition)
# 3. All numbers are +ve                                (Allows for pruning totals > target)

# Approach 1: Backtracking
# Example: candidates = [2,5,2,1,2], target = 5, expected answer = [ [1,2,2], [5] ]
# Short recursion of paths only
# path: [] idx: 0
#   path: [1] idx: 1
#     path: [1, 2] idx: 2
#       path: [1, 2, 2] idx: 3
#       path: [1, 2, 5] idx: 5
#     path: [1, 5] idx: 5
#   path: [2] idx: 2
#     path: [2, 2] idx: 3
#       path: [2, 2, 2] idx: 4
#       path: [2, 2, 5] idx: 5
#     path: [2, 5] idx: 5
#   path: [5] idx: 5

# Detailed recursion tree with path, index, target and result, and pruned paths
# bt call with idx: 0 path: [] target: 5 result: []
# checking next candidate for use or prune idx: 0, candidate: 1
#     bt call with idx: 1 path: [1] target: 4 result: []
#     checking next candidate for use or prune idx: 1, candidate: 2
#         bt call with idx: 2 path: [1, 2] target: 2 result: []
#         checking next candidate for use or prune idx: 2, candidate: 2
#             bt call with idx: 3 path: [1, 2, 2] target: 0 result: []
#             bt retn with idx: 3 path: [1, 2, 2] target: 0 result: []        - Pushing to result and returning cuz target achieved
#         checking next candidate for use or prune idx: 3, candidate: 2       - Duplicate path pruned
#         checking next candidate for use or prune idx: 4, candidate: 5
#         bt retn with idx: 2 path: [1, 2] target: 2 result: [[1, 2, 2]]
#     checking next candidate for use or prune idx: 2, candidate: 2           - Duplicate path pruned
#     checking next candidate for use or prune idx: 3, candidate: 2           - Duplicate path pruned
#     checking next candidate for use or prune idx: 4, candidate: 5
#     bt retn with idx: 1 path: [1] target: 4 result: [[1, 2, 2]]
# checking next candidate for use or prune idx: 1, candidate: 2
#     bt call with idx: 2 path: [2] target: 3 result: [[1, 2, 2]]
#     checking next candidate for use or prune idx: 2, candidate: 2
#         bt call with idx: 3 path: [2, 2] target: 1 result: [[1, 2, 2]]
#         checking next candidate for use or prune idx: 3, candidate: 2
#         bt retn with idx: 3 path: [2, 2] target: 1 result: [[1, 2, 2]]
#     checking next candidate for use or prune idx: 3, candidate: 2
#     checking next candidate for use or prune idx: 4, candidate: 5
#     bt retn with idx: 2 path: [2] target: 3 result: [[1, 2, 2]]
# checking next candidate for use or prune idx: 2, candidate: 2
# checking next candidate for use or prune idx: 3, candidate: 2
# checking next candidate for use or prune idx: 4, candidate: 5
#     bt call with idx: 5 path: [5] target: 0 result: [[1, 2, 2]]
#     bt retn with idx: 5 path: [5] target: 0 result: [[1, 2, 2]]
# bt retn with idx: 0 path: [] target: 5 result: [[1, 2, 2], [5]]


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(combination_sum2([10,1,2,7,6,1,5], 8), [
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
])
assert_equal(combination_sum2([2,5,2,1,2], 5), [
    [1,2,2],
    [5]
])


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
