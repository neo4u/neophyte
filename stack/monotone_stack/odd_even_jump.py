from typing import List

class Solution2:
    def oddEvenJumps(self, A: 'List[int]') -> 'int':
        # sort indexes of A by values in A
        sorted_indexes = sorted(range(len(A)), key=lambda i: A[i])

        # generate list of indexes we can jump to next on odd jumps
        oddnext = self.makeStack(sorted_indexes)

        # sort indexes of A by reverse order of their value in A
        sorted_indexes.sort(key=lambda i: A[i], reverse=True)

        # generate list of indexes we can jump to next on even jumps
        evennext = self.makeStack(sorted_indexes)

        # initialize odd and even lists that will contain
        # the information of if the end can be reached
        # from the respective index
        odd = [False] * len(A)
        even = [False] * len(A)

        # the last index is always counted
        odd[len(A)-1] = even[len(A)-1] = True

        # iterate through A backwards, starting at next to last element
        for i in range(len(A)-2, -1, -1):

            # if an odd jump is available from current index,
            # check if an even jump landed on the index of the available
            # odd jump and set current index in odd to True if it did
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]

            # if an even jump is available from current index,
            # check if an odd jump landed on the index of the available
            # even jump and set current index in even to True if it did
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        # return the number of spots marked True in odd
        # we always start with an odd jump, so odd will
        # contain the number of valid jumps to reach the end
        return sum(odd)

    # makes monotonic stack
    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        # delete stack as a memory optimization
        del stack
        return result




class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)

        idxs_sorted_by_value = sorted(range(n), key=lambda i: A[i])
        odd_next_hops = self.get_next_hops(idxs_sorted_by_value)

        idxs_sorted_by_value.sort(key=lambda i: -A[i])
        even_next_hops = self.get_next_hops(idxs_sorted_by_value)
        print(odd_next_hops)
        print(even_next_hops)

        odd, even = [False] * n, [False] * n
        odd[-1], even[-1] = True, True

        for i in reversed(range(n - 1)): # n - 2 to 0
            odd_next_hop, even_next_hop = odd_next_hops[i], even_next_hops[i]
            if odd_next_hop: odd[i] = even[odd_next_hop]
            if even_next_hop: even[i] = odd[even_next_hop]

        return sum(odd)

    def get_next_hops(self, idxs_sorted_by_value):
        next_hop = [None] * len(idxs_sorted_by_value)
        stack = []

        for i in idxs_sorted_by_value:
            while stack and stack[-1] < i:
                next_hop[stack.pop()] = i
            stack.append(i)

        return next_hop



# 975. Odd Even Jump
# https://leetcode.com/problems/odd-even-jump/description/


# Explanation of the problem:
# 1. Odd and even here refer to the 1st jump (odd jump) 2nd jump (even jump) 3rd jump (odd jump again) and so on.
# 2. We only jump forward always i < j
# 3. During odd jumps we can jump such that, A[i] <= A[j] and j is the smallest such index
#    During even jumps we can jump such that, A[i] >= A[j] and j is the smallest such index
# 4. We need to return how many indexes can actually reach the end using this kind of jump
# 5. We assume that last position is reachable from an odd and even jump

# Approach 1: Monotone Stack
# Time: O(n * log(n))
# Space: O(n)

# Steps:
# 1. Get the indexes of elements when the array is sorted by increasing value
# 2. Get the indexes of elements when the array is sorted by decreasing value
# 3. Now, we use a monotonically decreasing stack
#    i.e. >= from left to right of the stack array or from bottom to top thinking of the stack ADT is monotonically decreasing
# 4. Find the next jump index for each index in odd_next_greater indexes
# 5. Find the next jump index for each index in even_next_lower indexes
# 6. Construct odd and even arrays where odd[i] or even[i] represent:
#    if we can get to the end from index i using an odd or even next hop respectively.
# 7. Return sum(odd) to see how many indexes actually get to the end. Why odd? Cuz 1st jump is an odd jump as 1 is odd.


sol = Solution()
sol.oddEvenJumps([10, 13, 12, 14, 15])

# Example:
# nums: [10, 13, 12, 14, 15]
# Step 1: indexes sorted by inc value at indexes: [0, 2, 1, 3, 4]
# Step 2: indexes sorted by dec value at indexes: [4, 3, 1, 2, 0]
# Step 3: odd_next_hops: [2, 3, 3, 4, None]
# Step 4: even_next_hops: [None, 2, None, None, None]
