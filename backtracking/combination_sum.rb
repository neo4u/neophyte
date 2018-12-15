# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
    return [] if !candidates || candidates.empty?
    # candidates.sort!() # Asymptotically this will be useful for pruning duplicate combinations like [1,2,3] and [3,2,1]
    bt(candidates, target)
end

def bt(candidates, target, idx = 0, path = [], result = [], total = 0)
    if total == target
        result.push(path)
        return
    end

    idx.upto(candidates.size - 1) do |i|
        next if total + candidates[i] > target
        bt(candidates, target, i, path + [candidates[i]], result, total + candidates[i])
    end

    result
end

# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

# Similar problem list
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/combination-sum/discuss/16496/Accepted-16ms-c++-solution-use-backtracking-easy-understand.

# Points to remember
# 1. No duplicates combinations in result               (So we should consider each unique combination only once)
# 2. Combination can contain a number any no. of times  (This means combination with repitition)
# 3. All numbers are +ve                                (Allows for pruning totals > target)

# Approach 1: Backtracking

# Example: candidates = [2,3,6,7], target = 7

# dfs call with idx: 0 path: [] result: [] total: 0
# check with next candidate and prune i: 0 | candidate: 2
#     dfs call with idx: 0 path: [2] result: [] total: 2
#     check with next candidate and prune i: 0 | candidate: 2
#         dfs call with idx: 0 path: [2, 2] result: [] total: 4
#         check with next candidate and prune i: 0 | candidate: 2
#             dfs call with idx: 0 path: [2, 2, 2] result: [] total: 6
#             check with next candidate and prune i: 0 | candidate: 2
#             check with next candidate and prune i: 1 | candidate: 3
#             check with next candidate and prune i: 2 | candidate: 6
#             check with next candidate and prune i: 3 | candidate: 7
#             dfs retrn with idx: 0 path: [2, 2, 2] result: [] total: 6
#         check with next candidate and prune i: 1 | candidate: 3
#             dfs call with idx: 1 path: [2, 2, 3] result: [] total: 7
#             dfs retrn with idx: 1 path: [2, 2, 3] result: [[2, 2, 3]] total: 7
#         check with next candidate and prune i: 2 | candidate: 6
#         check with next candidate and prune i: 3 | candidate: 7
#         dfs retrn with idx: 0 path: [2, 2] result: [[2, 2, 3]] total: 4
#     check with next candidate and prune i: 1 | candidate: 3
#         dfs call with idx: 1 path: [2, 3] result: [[2, 2, 3]] total: 5
#         check with next candidate and prune i: 1 | candidate: 3
#         check with next candidate and prune i: 2 | candidate: 6
#         check with next candidate and prune i: 3 | candidate: 7
#         dfs retrn with idx: 1 path: [2, 3] result: [[2, 2, 3]] total: 5
#     check with next candidate and prune i: 2 | candidate: 6
#     check with next candidate and prune i: 3 | candidate: 7
#     dfs retrn with idx: 0 path: [2] result: [[2, 2, 3]] total: 2
# check with next candidate and prune i: 1 | candidate: 3
#     dfs call with idx: 1 path: [3] result: [[2, 2, 3]] total: 3
#     check with next candidate and prune i: 1 | candidate: 3
#         dfs call with idx: 1 path: [3, 3] result: [[2, 2, 3]] total: 6
#         check with next candidate and prune i: 1 | candidate: 3
#         check with next candidate and prune i: 2 | candidate: 6
#         check with next candidate and prune i: 3 | candidate: 7
#         dfs retrn with idx: 1 path: [3, 3] result: [[2, 2, 3]] total: 6
#     check with next candidate and prune i: 2 | candidate: 6
#     check with next candidate and prune i: 3 | candidate: 7
#     dfs retrn with idx: 1 path: [3] result: [[2, 2, 3]] total: 3
# check with next candidate and prune i: 2 | candidate: 6
#     dfs call with idx: 2 path: [6] result: [[2, 2, 3]] total: 6
#     check with next candidate and prune i: 2 | candidate: 6
#     check with next candidate and prune i: 3 | candidate: 7
#     dfs retrn with idx: 2 path: [6] result: [[2, 2, 3]] total: 6
# check with next candidate and prune i: 3 | candidate: 7
#     dfs call with idx: 3 path: [7] result: [[2, 2, 3]] total: 7
#     dfs retrn with idx: 3 path: [7] result: [[2, 2, 3], [7]] total: 7
# dfs retrn with idx: 0 path: [] result: [[2, 2, 3], [7]] total: 0
# Refer to the diagram for recursion tree

# Same as permutations i, ii,
# same as combination sum i, ii, iii
# Similar to generate parantheses and word break II in terms of backtracking technique

require 'test/unit'
extend Test::Unit::Assertions

assert_equal(combination_sum([2,3,6,7], 7), [[2, 2, 3], [7]])
assert_equal(combination_sum([2,3,5], 8), [
    [2,2,2,2],
    [2,3,3],
    [3,5]
])
