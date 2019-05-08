// 658. Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/description/

public class Solution {
    public List<Integer> findClosestElements(int[] nums, int k, int target) {
        List<T> arr = Arrays.asList(nums);

        int n = arr.size();
        if (target <= arr.get(0)) {
            return arr.subList(0, k);
        } else if (arr.get(n - 1) <= target) {
            return arr.subList(n - k, n);
        } else {
            int index = Collections.binarySearch(arr, target);
            if (index < 0) // index = -1
                index = -index - 1; // index = -(-1) -1 = 1-1 = 0
            int low = Math.max(0, index - k - 1), high = Math.min(arr.size() - 1, index + k - 1);

            while (high - low > k - 1) {
                if (low < 0 || (target - arr.get(low)) <= (arr.get(high) - target))
                    high--;
                else if (high > arr.size() - 1 || (target - arr.get(low)) > (arr.get(high) - target))
                    low++;
                else
                    System.out.println("unhandled case: " + low + " " + high);
            }
            return arr.subList(low, high + 1);
        }
    }
}
