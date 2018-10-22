# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    l, r = 1, n

    while l < r
        mid = (l + r)/ 2
        
        is_bad_version(mid) ? r = mid : l = mid + 1
    end

    l
end


# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# Approach binary search
# start from middle if you find that the mid is bad then you know the answer is to the left of it,
# So we abandon the right half, right of mid to end. This can be achieved by setting r to mid

# If you are setting mid=(left+right)/2, you have to be very careful.
# Unless you are using a language that does not overflow such as Python,
# left + right could overflow. One way to fix this is to use left + (right − left)/2 instead.

# Complexity analysis
# Time: O(logn). The search space is halved each time, so the time complexity is O(logn).
# Space: O(1).