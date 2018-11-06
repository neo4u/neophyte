# The knows API is already defined for you.
# @param {Integer} person a
# @param {Integer} person b
# @return {Boolean} whether a knows b
# def knows(a, b)

# @param {Integer} n
# @return {Integer}
def find_celebrity(n)
    candidate = 0

    1.upto(n - 1) do |i|
        candidate = i if knows(candidate, i)
    end

    0.upto(n - 1) do |i|
        return -1 if i != candidate && (knows(candidate, i) || !knows(i, candidate))
    end

    candidate
end

# 277. Find the Celebrity
# https://leetcode.com/problems/find-the-celebrity/

# Approach: Two Pass
# 1. Do a first pass to pick candidate starting from 0
#    and replacing candidates who know current person with current persion
# 2. Second pass to validate picked candidate as a celeb by checking definition that
#    1. candidate shouldn't know anyone
#    2. everyone should know candidate

# Time: O(n) calls to knows
# Space: O(1)