// We want to check mid and mid+1 elements.
// if(nums[mid] < nums[mid+1]), lo = mid + 1, otherwise hi = mid.
// The reason is that when there are even or odd number of elements,
// the mid element is always going to have a next one mid+1.
// We don't need to consider the case when there is less than 1 element
// as it is not valid case for this problem.
// Finally we return lo as it will always be a solution
// since it goes to mid+1 element in the first case, which is larger.

public int findPeakElement(int[] nums) {
    int n = nums.length;
    int lo = 0, hi = n - 1;

    while(lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if(nums[mid] < nums[mid+1]) {
            lo = mid + 1; 
        } else {
            hi = mid;
        }
    }

    return lo;
}