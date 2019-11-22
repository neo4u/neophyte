# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.q = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0

        while self.q and n:
            buf[idx] = self.q.pop(0)
            idx += 1; n -= 1
            

        while n:
            buf4 = [''] * 4
            count = read4(buf4)
            if not count: return idx # EOF

            if count > n:               # We called read with n = 1 but read4 returned 4, we need to cache 3 chars
                self.q += buf4[n:]      # Think of this as taking what you need this run, and saving the rest for next run, Same as buf4[n:count]

            for i in range(min(count, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1

        return idx


# 158. Read N Characters Given Read4 II - Call multiple times
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/

# Approach
# Difference from the first instance is that we can call read in parts, and some part can be less than 4
# But we have to call read4 so in that case we need a cache for our 3 uncalled chars
# We use a instance variable that stores last uncalled chars

# Apart from that approach remains same except step 6
# 1. maintain a pointer for 1 more than last index of buffer, this will be the final return
# 2. capture read4 into buf4 of length 4
# 3. copy over buf4 into read4, while decrementing n and incrementing buffer index
# 4. the tricky part is when at the end only < 4 chars are returned or when less than 4 chars are called
# 5. If < 4 are return, At that point take min of return count and remaining n and copy over the chars from buff for those many times
# 6. if < 4 are called, then buffer them in instance variable q.

# Time: O(n)
# Space: O(1)
