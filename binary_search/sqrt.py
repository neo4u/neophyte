# Binary search  
def mySqrt(self, x):
    l, r = 0, x
    while l <= r:
        mid = l + (r-l)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            r = mid
        else:
            l = mid + 1


def mySqrt(self, x):
    l,r = 0,x
    while l < r:
        mid = (l+r) // 2
        if x < mid*mid:
            r = mid
        else:
            l = mid + 1
    return l-1 if l>1 else l # careful about 0,1 cases