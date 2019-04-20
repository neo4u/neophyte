# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer[][]}
def k_closest(points, k)
    n = points.size
    return [] if k == 0
    return points if n == k

    @dist = points.map { |x, y| x**2 + y**2 }
    p @dist
    quick_select(points, 0, n - 1, k)
end

def quick_select(a, p, r, k)
    puts "quick_select p: #{p}, r: #{r}, k: #{k}"
    return a[p] if p == r               # Base case of recursion
    q = rand_partition(a, p, r)         # Pick the pivot using random partition
    puts "q: #{q} | a: #{a}"
    if k < q
        quick_select(a, p, q - 1, k)    # kth smallest is in the lower partition
    elsif k > q
        quick_select(a, q + 1, r, k)    # kth smallest is in the higher partition
    else
        a[q]                            # if q == k return Pivot as the kth smallest
    end

    a
end

def rand_partition(a, p, r)
    i = rand(p..r)                 # Pick a random index between p and r - 1 inclusive
    puts "i: #{i}, p: #{p}, r: #{r}"
    a[i], a[r] = a[r], a[i]             # Swap the last element with the one at i

    partition(a, p, r)                  # Return result of partition()
end

def partition(a, p, r)
    puts "partition -> p: #{p}, r: #{r}"
    i = p - 1                           # Choose the index before the pth index
    pivot = @dist[r]                    # Choose the last element as pivot

    p.upto(r - 1) do |j|                # Loop from p to r-1 moving elements to either side of pivot
        next if @dist[j] > pivot          # Move to next element if element is already > than pivot element
        i += 1                            # Increment index i for current pivot placement index
        a[i], a[j] = a[j], a[i]           # Swap elements at pivot placement index with the current index j
    end
  
    a[i + 1], a[r] = a[r], a[i + 1]     # Move the pivot to its final place: index before which all elements < pivot
    i + 1                               # return pivot index
end


# class Solution(object):
#     def kClosest(self, points, K):
#         dist = lambda i: points[i][0]**2 + points[i][1]**2

#         def sort(i, j, K):
#             # Partially sorts A[i:j+1] so the first K elements are
#             # the smallest K elements.
#             if i >= j: return

#             # Put random element as A[i] - this is the pivot
#             k = random.randint(i, j)
#             points[i], points[k] = points[k], points[i]

#             mid = partition(i, j)
#             if K < mid - i + 1:
#                 sort(i, mid - 1, K)
#             elif K > mid - i + 1:
#                 sort(mid + 1, j, K - (mid - i + 1))

#         def partition(i, j):
#             # Partition by pivot A[i], returning an index mid
#             # such that A[i] <= A[mid] <= A[j] for i < mid < j.
#             oi = i
#             pivot = dist(i)
#             i += 1

#             while True:
#                 while i < j and dist(i) < pivot:
#                     i += 1
#                 while i <= j and dist(j) >= pivot:
#                     j -= 1
#                 if i >= j: break
#                 points[i], points[j] = points[j], points[i]

#             points[oi], points[j] = points[j], points[oi]
#             return j

#         sort(0, len(points) - 1, K)
#         return points[:K]

# Approach 1: Sort
# Steps:
# 1. Sort using distances (x^2 + y^2) as key for sorting the given points
# 2. Select the first k elements
# Time: O(nlog(n))
# Space: O(1)

require 'test/unit'
extend Test::Unit::Assertions

# assert_equal(k_closest([[0,1],[1,0]], 2), [[0,1],[1,0]])
# assert_equal(k_closest([[1,3],[-2,2]], 1), [[-2,2]])
assert_equal(k_closest([[3,3],[5,-1],[-2,4]],2), [[3,3],[-2,4]])
