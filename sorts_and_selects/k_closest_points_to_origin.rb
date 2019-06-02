def k_closest(points, k)
    n = points.size
    return [] if k == 0
    return points if n == k
    quick_select(points, 0, n - 1, k)
    points[0...k]
end

def dist(x, y)
    x**2 + y**2
end

def quick_select(a, l, r, k)            # Note the k here refers to (n - k) from the question stand-point
    return if l == r                    # Base case of recursion
    mid = rand_partition(a, l, r)         # Pick the pivot using random partition

    if k < mid
        quick_select(a, l, mid - 1, k)    # kth smallest is in the lower partition
    elsif k > mid
        quick_select(a, mid + 1, r, k)    # kth smallest is in the higher partition
    else
        return
    end
end

def rand_partition(a, l, r)
    i = rand(l...r)                      # Pick a random index between p and r - 1 inclusive
    a[i], a[r] = a[r], a[i]             # Swap the last element with the one at i

    partition(a, l, r)                  # Return result of partition()
end

def partition(a, l, r)
    i = l - 1                           # Choose the index before the pth index
    pivot = dist(*a[r])                  # Choose the last element as pivot

    l.upto(r - 1) do |j|                # Loop from p to r-1 moving elements to either side of pivot
      next if dist(*a[j]) > pivot        # Move to next element if element is already > than pivot element
      i += 1                            # Increment index i for current pivot placement index
      a[i], a[j] = a[j], a[i]           # Swap elements at pivot placement index with the current index j
    end
  
    a[i + 1], a[r] = a[r], a[i + 1]     # Move the pivot to its final place: index before which all elements < pivot
    i + 1                               # return pivot index
end


# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/


# Approach 1: Sort
# Steps:
# 1. Sort using distances (x^2 + y^2) as key for sorting the given points
# 2. Select the first k elements

# Time: O(nlog(n))
# Space: O(1)

# Approach 2: Quick Select (Optimal)
# Steps:
# 1. Do quick select on points to get k smallest distances
# 2. while partitioning them, use distance of the point from origin as pivot

# Time: O(n)
# Space: O(log(n))


require 'test/unit'
extend Test::Unit::Assertions

assert_equal(k_closest([[0,1],[1,0]], 2), [[0,1],[1,0]])
assert_equal(k_closest([[1,3],[-2,2]], 1), [[-2,2]])
assert_equal(k_closest([[3,3],[5,-1],[-2,4]],2), [[3,3],[-2,4]])
