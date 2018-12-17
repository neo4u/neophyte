# Segment Tree
class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n - 1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + end >> 1
        root.children = filter(None, [
            self.build(start, end)
            for start, end in ((start, mid), (mid + 1, end))])
        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return root.val

        if i == root.start == root.end:
            root.val += val
            return root.val

        root.val = sum([self.update(i, val, c) for c in root.children])
        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0

        if start <= root.start and end >= root.end:
            return root.val

        return sum([self.sum(start, end, c) for c in root.children])

class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = SegmentTree(len(hashTable)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(0, hashTable[nums[i]] - 1))
            tree.update(hashTable[nums[i]], 1)
        return r[::-1]


# Binary Indexed Tree
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r

class Solution(object):
    def countSmaller(self, nums):
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree, r = BinaryIndexedTree(len(hashTable)), []
        for i in xrange(len(nums) - 1, -1, -1):
            r.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]


# Solution
# Binary Search Tree (1)
# Iterate over the input array in reverse order.
# Keep adding each element into a BST.
# In one method, store the count of the number of nodes rooted at that node.
# Pay special attention towards handling duplicates.
# While inserting element val (i index), if root.val < t,
# then we update the number of elements lesser by root.dupe + size(root.left).
# We can maintain a count of this variable while inserting into the tree itself.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        # self.count is the size of the subtree rooted at this node.
        # self.dupe is the frequency of the value.
        self.count, self.dupe = 1, 1

class Solution(object):
    def size(self, root):
        if root == None:
            return 0
        return root.count
    
    def insert(self, root, val):
        # This method inserts into the BST.
        # It also updates root.dupe which is the frequency of the value.
        # It also updates root.count which is the size of the sub-tree rooted at root.        
        if root == None:
            root = Node(val)
        elif root.val == val:
            root.dupe += 1
        elif root.val < val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        root.count = self.size(root.left) + self.size(root.right) + root.dupe
        return root

    def find(self, root, t):
        count = 0
        while root:
            # 1: If the value is equal to the value inside root, then the number of values less than val is size of left sub-tree.
            # 2: If the value is more then the value inside root, then elements less are equal to size of left tree + dupes.
            # 3: If the value is less than the value inside root, then move left.
            if root.val == t:
                count += self.size(root.left)
                break
            elif root.val < t:
                count += root.dupe + self.size(root.left)
                root = root.right
            else:
                root = root.left
        return count

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        N = len(nums)
        root, counts = self.insert(None, nums[-1]), [0]*N
        for i in range(N-2, -1, -1):
            ### This is now a rank() problem. For the ith element, we have a BST with all 
            ### elements to its right. Simply pass num[i] to find the rank or elements less than num[i].
            counts[i] = self.find(root, nums[i])
            root = self.insert(root, nums[i])
        return counts

# Binary Search Tree (2)
# We need not call find - insertion and find logic can be merged.
class Solution(object):
    def size(self, root):
        if root == None:
            return 0
        return root.count
    
    def insert(self, root, val):
        if root == None:
            root = Node(val)
        elif root.val == val:
            root.dupe = root.dupe + 1
            self.less_count = self.less_count + self.size(root.left)
        elif root.val < val:
            root.right = self.insert(root.right, val)
            self.less_count = self.less_count + root.dupe + self.size(root.left)
        else:
            root.left = self.insert(root.left, val)
        root.count = self.size(root.left) + self.size(root.right) + root.dupe
        return root    
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        root, counts = None, [0]*N
        for i in range(N-1, -1, -1):
            self.less_count = 0
            root = self.insert(root, nums[i])
            counts[i] = self.less_count
        return counts


# Binary Search Tree (3) - Itervaitve
# Another appproach is to store the number of elements
# less than the node in its count field.
# A nice iterative algorithm can be built for this approach.
# You can update the count (i.e. number of elements
# less than the current element) using this update rule
# if val <= root.val: root.count = root.count + 1
# We keep a count variable to track the number of nodes less than val.
# This is updated only when val > root.val using count = count + root.count.
# Again this can be maintained while insertion.
class Node1(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        # self.count is the size of the left-subtree plus number of times val is repeated.
        # No need for dupe here.
        self.count = 1
        return

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        root, counts = None, [0]*N
        for i in range(N-1, -1, -1):
            if root == None:
                root = Node1(nums[i])
                continue
            counts[i] = self.insert(root, nums[i])
        return counts
    
    def insert(self, root, val):
        count = 0
        while True:
            if val <= root.val:
                root.count = root.count + 1
                if root.left == None:
                    root.left = Node1(val)
                    break
                else:
                    root = root.left
            else:
                count = count + root.count
                if root.right == None:
                    root.right = Node1(val)
                    break
                else:
                    root = root.right
        return count


# Merge Sort Implementation
# Study implementation of merge-sort.
# Now extend the idea of merge sort to the problem of counting inversions.
# During the merge process, say i is left index and j is the right index.
# If a[i] > a[j], we have an inversion. Increment the variable inversion by 1 and place a[j] in result array.
# When we have a[i] <= a[j], the value of the variable inversion is exactly the number of elements in right array less than a[i]. So update count[i] with this value. Then place a[i] in results array. We do the same thing when j == high+1: Example: [5,6,7] and [1,2,3] and imagine j is now 3 and inversions variable is 3. Therefore, we add 3 to the count of inversions for 5,6,7.
# Also notice that the inversion count is never reset. The inversions for a[i+1] are atleast as much as inversions for a[i] since a[i+1] >= a[i]. [20.22,28,30] and [10,12,33,38]. Run over this example.
# Note the implementation as well - we do not reset inversions ever. Also we transform nums into an array of tuples with value and original index. Lastly the counts array is used to continously update the inversion count for an index.
class Solution(object):
    def merge(self, nums, aux, count, low, mid, high):
        for i in range(low, high+1):
            aux[i] = nums[i]
        i,j,inversions = low, mid+1,0
        for k in range(low, high+1):
            if i == mid+1:
                nums[k],j = aux[j],j+1
            elif j == high + 1 or aux[i][1] <= aux[j][1]:
                count[aux[i][0]] = count[aux[i][0]] + inversions
                nums[k] , i= aux[i], i+1
            elif aux[j][1] < aux[i][1]:
                inversions = inversions + 1
                nums[k], j = aux[j], j+1
        return

    def mergesort(self, nums, aux, count, low, high):
        if low >= high:
            return
        mid = low + (high-low)//2
        self.mergesort(nums, aux, count, low, mid)
        self.mergesort(nums, aux, count, mid+1, high)
        self.merge(nums, aux, count, low, mid, high)    
        return
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums, aux, counts = list(enumerate(nums)), [0]*len(nums), [0]*len(nums)
        self.mergesort(nums, aux, counts, 0, len(nums)-1)
        return counts


# Implementation of Merge-Sort
# Here is an implementation of merge-sort!
class Solution_implement_merge_sort(object):
    def merge(nums, aux, low, mid, high):
        for i in range(low, high+1):
            aux[i] = nums[i]
        i,j = low, mid+1
        for k in range(low, high+1):
            if i == mid+1:
                nums[k],j = aux[j],j+1
            elif j == high + 1:
                nums[k], i = aux[i], i+1
            elif aux[i] <= aux[j]:
                nums[k] , i= aux[i], i+1
            else:
                nums[k], j = aux[j], j+1
        return

    def mergesort(nums, aux, low, high):
        if low >= high:
            return
        mid = low + (high-low)//2
        mergesort(nums, aux, low, mid)
        mergesort(nums, aux, mid+1, high)
        merge(nums, aux, low, mid, high)
        return

    def sort(nums):
        aux = [0]*len(nums)
        mergesort(nums, aux, 0, len(nums) - 1)
        return


# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# Approach 1: Segment Tree
# Approach 2: Binary Indexed Tree
# Approach 3: Binary Search Tree
# Approach 4: Merge-sort
# MergeSort-based solution is a standard way to solve problems related to inverse numbers.

# Here is an example to illustrate the general idea of MergeSort-based algorithm:
# Now we want to consider an array
#             6 4 1 8 7 5 2 9

# First thing first, split the array into to subarrays:
#             6 4 1 8
#             7 5 2 9

# and then calculate the inverse numbers within the group:
#                   1 4(1) 6(1,4) 8
#                   2 5(2) 7(2,5) 9
# where the numbers in the parentheses are the numbers that should be counted when we calculate the inverse number.

# Now we need to merge these two arrays into one sorted array. The first element to be put into the sorted destination array is the "1" in the first array.
#  1                  4(1) 6(1,4) 8
#                   2 5(2) 7(2,5) 9               merged elements in the 2nd array = ()

# The second element to merge is the "2" in the second array:
#  1 2                4(1) 6(1,4) 8
#                     5(2) 7(2,5) 9               merged elements in the 2nd array = (2)

# The third element to merge is the "4" in the first array:
#  1 2 4(1,2)              6(1,4) 8
#                     5(2) 7(2,5) 9               merged elements in the 2nd array = (2)

# When we merge the "4(1)", we found that "4" is actually greater than all merged elements in the second array (i.e. [2]). Therefore, we also need to consider those elements. Therefore, the numbers in the parenthese of 2 become (1)+(2) = (1,2). Next step:
#  1 2 4(1,2) 5(2)         6(1,4) 8
#                          7(2,5) 9               merged elements in the 2nd array = (2,5)

# Next (add the inverse number of element "6" by 2)
#  1 2 4(1,2) 5(2) 6(1,4,2,5)     8
#                          7(2,5) 9               merged elements in the 2nd array = (2,5)

# So and so forth, finally reach
#  1 2 4(1,2) 5(2) 6(1,4,2,5) 7(2,5) 8(2,5,7) 9
#                                                 merged elements in the 2nd array = (2,5,7,9)
# Additionally, when we need to count the inverse number, we do not need to record the exact elements, we only need to record the numbers. So, we can use a variable to record the number of "merged elements in the 2nd array" (for example, semilen in the code beneath) and the number of smaller elements of each element (for example, results[idx] in the code beneath).

# Complexities:
# Time: O(n log n)
# Space: O(n)