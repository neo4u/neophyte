# [5, 10, 30, 2, 1, 0, 10]
# n = len(bar)

def min_max_chocolate_bar(bar):
    n = len(bar)
    min_val = float('inf')
    max_min = -float('inf')
    for i in range(1, n):
        for j in range(n - i):
            sum = sum(bar[j:i])
            if sum < min_val: min_val = sum
            if min_val > max_min: max_min = min_val

    return max_min

# https://www.geeksforgeeks.org/divide-array-k-segments-maximize-maximum-segment-minimums/