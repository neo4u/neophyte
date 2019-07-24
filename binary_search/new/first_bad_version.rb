# The is_bad_version API is already defined for you.
# @param {Integer} version
# @return {boolean} whether the version is bad
# def is_bad_version(version):

# @param {Integer} n
# @return {Integer}
def first_bad_version(n)
    l, r = 1, n

    while l < r
        mid = (l + r) / 2
        is_bad_version(mid) ? r = mid : l = mid + 1
    end

    l
end



# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

# Approach #2 (Binary Search) [Accepted]
# It is not difficult to see that this could be solved using a classic algorithm - Binary search.
# Let us see how the search space could be halved each time below.

# Scenario #1: isBadVersion(mid) => false
#  1 2 3 4 5 6 7 8 9
#  G G G G G G B B B       G = Good, B = Bad
#  |       |       |
# left    mid    right
# Let us look at the first scenario above where isBadVersion(mid) \Rightarrow falseisBadVersion(mid)⇒false. We know that all versions preceding and including midmid are all good. So we set left = mid + 1left=mid+1 to indicate that the new search space is the interval [mid + 1, right][mid+1,right] (inclusive).

# Scenario #2: isBadVersion(mid) => true
#  1 2 3 4 5 6 7 8 9
#  G G G B B B B B B       G = Good, B = Bad
#  |       |       |
# left    mid    right

# The only scenario left is where isBadVersion(mid) ⇒ true.
# This tells us that midmid may or may not be the first bad version,
# but we can tell for sure that all versions after midmid can be discarded.
# Therefore we set right = midright=mid as the new search space of interval [left,mid][left,mid] (inclusive).

# In our case, we indicate leftleft and rightright as the boundary of our search space (both inclusive).
# This is why we initialize left = 1left=1 and right = n right = n.
# How about the terminating condition? We could guess that leftleft and rightright
# eventually both meet and it must be the first bad version, but how could you tell for sure?

# The formal way is to prove by induction, which you can read up yourself if you are interested.
# Here is a helpful tip to quickly prove the correctness of your binary search algorithm during an interview.
# We just need to test an input of size 2.
# Check if it reduces the search space to a single element (which must be the answer)
# for both of the scenarios above. If not, your algorithm will never terminate.

# If you are setting mid = left+right, you have to be very careful.
# Unless you are using a language that does not overflow such as Python, left + right could overflow.
# One way to fix this is to use left + (right−left)/2 instead.

# If you fall into this subtle overflow bug, you are not alone.
# Even Jon Bentley's own implementation of binary search had this overflow
# bug and remained undetected for over twenty years.

# Time: O(logn), The search space is halved each time, so the time complexity is O(logn).
# Space: O(1)