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

def first_bad_version(n)
    l, r = 1, n

    while l <= r
        mid = (l + r)/ 2
        is_bad_version(mid) ? r = mid - 1 : l = mid + 1
    end

    l
end


# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# Approach binary search
# 1. Find mid and check if bad
# 2. If bad, you know that everything to right is bad
#    and we want to find the first bad one so search left (r = mid)
# 3. If good, then you know everything before you is good so bad must to the right (l = mid + 1)

# If you are setting mid=(left+right)/2, you have to be very careful.
# Unless you are using a language that does not overflow such as Python,
# left + right could overflow. One way to fix this is to use left + (right − left)/2 instead.

# Complexity analysis
# Time: O(logn). The search space is halved each time, so the time complexity is O(logn).
# Space: O(1).